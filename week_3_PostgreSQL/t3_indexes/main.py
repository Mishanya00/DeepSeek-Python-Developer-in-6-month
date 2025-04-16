from datetime import datetime
import asyncio
import asyncpg

from config import DB_CONFIG
from names import popular_names
from random import choice


async def drop_table(pool: asyncpg.Pool):
    async with pool.acquire() as aconn:
        await aconn.execute('DROP TABLE IF EXISTS users')


async def create_table(pool: asyncpg.Pool):
    async with pool.acquire() as aconn:
        await aconn.execute(
            """
                CREATE TABLE IF NOT EXISTS users (
                        id SERIAL PRIMARY KEY,
                        name TEXT,
                        signup_date DATE
                        )
                        """
        )
    

async def create_user(pool: asyncpg.Pool, name: str):
    async with pool.acquire() as aconn:
        result = await aconn.fetchrow(f'INSERT INTO users(name, signup_date) VALUES ($1, $2)', name, datetime.now())
        return result
    

async def create_10k_users(pool: asyncpg.Pool):
    start = datetime.now()
    for i in range(10**4):
        await create_user(pool, choice(popular_names))
    finish = datetime.now()
    print('Time to add 10k users:', finish-start)


async def main():
    conn_string = f"postgresql://{DB_CONFIG['username']}:{DB_CONFIG['password']}@{DB_CONFIG['host']}/{DB_CONFIG['dbname']}"

    asyncpg_pool = await asyncpg.create_pool(conn_string)

    await drop_table(asyncpg_pool)
    await create_table(asyncpg_pool)


asyncio.run(main())