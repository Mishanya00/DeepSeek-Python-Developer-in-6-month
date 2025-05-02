import time
from functools import lru_cache
from typing import Annotated

from fastapi import FastAPI, Request, Depends
from fastapi.responses import JSONResponse
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "W4D1 (Week 4 Day 1) App"
    api_key: str = "incorrect_api_key_by_default_xxxxxxx"

    model_config = SettingsConfigDict(env_file=".env")


@lru_cache
def get_settings_cached():
    return Settings()


def get_settings():
    # useless piece of code to show difference in time between two dependencies
    a = 11
    for i in range(1000000):
        a += 1
    return Settings()


app = FastAPI()


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.perf_counter()
    response = await call_next(request)
    process_time = time.perf_counter() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response


@app.middleware("http")
async def uniform_error_handler(request: Request, call_next):
    try:
        return await call_next(request)
    except ZeroDivisionError as e:
                return JSONResponse(
            status_code=500,
            content={"error": "Wow, you took a risk! Nice move :)", "details": str(e)}
        )
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"error": "Oh, we got an error here! Sorry :(", "details": str(e)}
        )


@app.get('/cached_config_info')
async def get_cached_config(settings: Annotated[Settings, Depends(get_settings_cached)]):
    # Never do it anywhere ! :) Its only for educational purpose
    return {
         "app name": settings.app_name,
         "api key": settings.api_key
    }


@app.get('/dynamic_config_info')
async def get_config(settings: Annotated[Settings, Depends(get_settings)]):
    # Never do it anywhere ! :) Its only for educational purpose
    return {
         "app name": settings.app_name,
         "api key": settings.api_key
    }


@app.get('/zero_division_error')
async def get_zero():
    1 / 0
    return {'mission': 'Impossible!'}


@app.get('/another_error')
async def get_error():
    raise KeyError
    return {'mission': 'Impossible!'}