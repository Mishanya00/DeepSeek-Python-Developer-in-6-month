from contextlib import asynccontextmanager
from fastapi import FastAPI
from database import setup_database


@asynccontextmanager
async def lifespan(app: FastAPI):
    await setup_database()
    yield


app = FastAPI(lifespan=lifespan)

