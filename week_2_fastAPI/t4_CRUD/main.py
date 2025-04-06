from typing import Annotated

from contextlib import asynccontextmanager

from sqlalchemy.ext.asyncio import AsyncSession

from fastapi import FastAPI, HTTPException
from fastapi import Query, Body, Path, Depends

from database import get_session, setup_database, create_user, get_items, create_item, delete_item


@asynccontextmanager
async def lifespan(app: FastAPI):
    await setup_database()
    yield


SessionDep = Annotated[AsyncSession, Depends(get_session)]

app = FastAPI(lifespan=lifespan)


@app.post("/users")
async def users_post(
    username: Annotated[str, Body(min_length=4)],
    password: Annotated[str, Body(min_length=8)],
    session: SessionDep,
):
    return await create_user(username, password, session)


@app.post("/items/{username}")
async def items_post(
    username: Annotated[str, Path()],
    item: Annotated[str, Body(max_length=255)],
    session: SessionDep,
):
    return await create_item(item, username, session)


@app.delete("/items/{username}")
async def items_delete(
    username: Annotated[str, Path()],
    password: Annotated[str, Query(min_length=8)],
    item: Annotated[str, Query(max_length=255)],
    session: SessionDep,
):
    result = await delete_item(username, password, item, session)
    if not result:
        return {'error': 'incorrect credentials or item'}
    else:
        return {"message": "Item successfully deleted!"}



@app.get("/items/{username}")
async def items_get(
    username: Annotated[str, Path()],
    password: Annotated[str, Query(min_length=8)], # not secure only for study purpose
    session: SessionDep,
):
    items = await get_items(username, password, session)
    if items is None:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return items
