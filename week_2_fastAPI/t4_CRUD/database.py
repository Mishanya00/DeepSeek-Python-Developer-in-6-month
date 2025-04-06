from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import selectinload
from sqlalchemy import select
from models import Base, User, Item


DATABASE_URL = "sqlite+aiosqlite:///data/users.db"

engine = create_async_engine(DATABASE_URL)

new_session = async_sessionmaker(engine, expire_on_commit=False)


async def get_session():
    async with new_session() as session:
        yield session


async def setup_database():
    async with engine.begin() as conn:
        # await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


async def create_user(username: str, password: str, session: AsyncSession):
    user = User(username=username)
    user.set_password(password)
    session.add(user)
    await session.commit()
    return user


async def create_item(item_name: str, username: str, session: AsyncSession):
    result = await session.execute(
        select(User)
        .where(User.username==username)
    )
    user = result.scalar_one_or_none()

    if not user:
        return None
    
    new_item = Item(name=item_name, user_id=user.id)
    session.add(new_item)
    await session.commit()
    return new_item


async def delete_item(username: str, password: str, item_name: str, session: AsyncSession):
    result = await session.execute(
        select(User)
        .where(User.username==username)
    )
    user = result.scalar_one_or_none()

    if not user or not user.verify_password(password):
        return False
    
    result = await session.execute(
        select(Item)
        .where(Item.name == item_name)
        .where(Item.user_id == user.id)
    )
    item = result.scalar_one_or_none()

    if item:
        await session.delete(item)
        await session.commit()
        return True
    
    return False


async def get_items(username: str, password: str, session: AsyncSession):
    result = await session.execute(
        select(User)
        .where(User.username == username)
        .options(selectinload(User.items))
    )
    user = result.scalar_one_or_none()

    if not user or not user.verify_password(password):
        return None
    return user.items