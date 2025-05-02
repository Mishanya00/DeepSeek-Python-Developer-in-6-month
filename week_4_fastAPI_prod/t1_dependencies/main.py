from functools import lru_cache
from typing import Annotated

from fastapi import Depends, FastAPI, Header, HTTPException
from pydantic_settings import BaseSettings, SettingsConfigDict


fake_db_users = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 32},
    {"name": "Charlie", "age": 41},
    {"name": "David", "age": 28},
    {"name": "Eve", "age": 35},
    {"name": "Jona", "age": 29},
    {"name": "Kevin", "age": 45},
    {"name": "Laura", "age": 31},
    {"name": "Mike", "age": 38},
    {"name": "Nancy", "age": 26}
]


# It automatically takes APP_NAME variable value, I didnt know :)
# To test in Win CMD: set APP_NAME=Wow-APP
class Settings(BaseSettings):
    app_name: str = "W4D1 (Week 4 Day 1) App"
    api_key: str = "incorrect_api_key_by_default_xxxxxxx"

    model_config = SettingsConfigDict(env_file=".env")


@lru_cache
def get_settings():
    return Settings()


app = FastAPI()


def api_key(key: Annotated[str, Header(min_length=32)], settings: Annotated[Settings, Depends(get_settings)]):
        if key != settings.api_key:
            raise HTTPException(status_code=400, detail="API key is invalid!")        
        return key


class UserFilter:
    def __init__(self, skip: int = 0, limit: int = 10):
        self.skip = skip
        self.limit = limit


@app.get('/')
async def hello():
    return {"message": "Hello!"}


@app.get('/config_info')
async def get_config(settings: Annotated[Settings, Depends(get_settings)]):
    # Never do it anywhere ! :) Its only for educational purpose
    return {
         "app name": settings.app_name,
         "api key": settings.api_key
    }


@app.get('/users', dependencies=[Depends(api_key)])
async def get_users(filter: Annotated[UserFilter, Depends()]):
    filtered_users = fake_db_users[filter.skip:filter.skip+filter.limit]
    return filtered_users