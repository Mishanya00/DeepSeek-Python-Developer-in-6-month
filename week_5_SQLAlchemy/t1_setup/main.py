import asyncio

from sqlalchemy import String
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column

from config import load_config


# I reckon I'm enough with sql queries so I will use ORM-ish style
class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'users_alchemy'

    user_id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String)
    email: Mapped[str] = mapped_column(String, unique=True)


async def main():
    DB_CONFIG = load_config()
    print(DB_CONFIG)

    conn_str = f"""postgresql+asyncpg://{DB_CONFIG["username"]}:{DB_CONFIG["password"]}@{DB_CONFIG["host"]}:5432/{DB_CONFIG["dbname"]}"""

    engine = create_async_engine(conn_str, echo=True)

    async with engine.begin() as aconn:
        print('TEST TEST TEST TEST')
        await aconn.run_sync(Base.metadata.create_all)


asyncio.run(main())
