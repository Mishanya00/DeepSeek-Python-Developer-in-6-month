from datetime import datetime
import asyncio
import asyncpg

from config import DB_CONFIG
from names import popular_names
from random import choice


random_names = [choice(popular_names) for i in range(10**4)]
random_names_to_select1 = [choice(popular_names) for i in range(10**4)]
random_names_to_select2 = [choice(popular_names[100:375:]) for i in range(10**4)]   # Not all possible names


async def drop_table(pool: asyncpg.Pool):
    async with pool.acquire() as aconn:
        await aconn.execute('DROP TABLE IF EXISTS users_indexes')


async def create_table(pool: asyncpg.Pool):
    async with pool.acquire() as aconn:
        await aconn.execute(
            """
                CREATE TABLE IF NOT EXISTS users_indexes (
                        id SERIAL PRIMARY KEY,
                        name TEXT,
                        signup_date DATE
                        )
                        """
        )


async def create_index(pool: asyncpg.Pool):
    async with pool.acquire() as aconn:
        # await aconn.execute('CREATE INDEX IF NOT EXISTS idx_name ON users_indexes USING HASH(name)')
        await aconn.execute('CREATE INDEX IF NOT EXISTS idx_name ON users_indexes(name)')


async def select_user(pool: asyncpg.Pool, name: str):
    async with pool.acquire() as aconn:
        result = await aconn.fetchrow('SELECT id, name, signup_date FROM users_indexes WHERE name = $1', name)
        return result
    

async def create_user(pool: asyncpg.Pool, name: str):
    async with pool.acquire() as aconn:
        result = await aconn.fetchrow(f'INSERT INTO users_indexes(name, signup_date) VALUES ($1, $2)', name, datetime.now())
        return result
    

async def create_10k_users(pool: asyncpg.Pool):
    start = datetime.now()
    for name in random_names:
        await create_user(pool, name)
    finish = datetime.now()
    print('Time to add 10k users:', finish-start)


async def select_10k_random_users(pool: asyncpg.Pool):
    start = datetime.now()
    for name in random_names_to_select2:
        await select_user(pool, choice(name))
    finish = datetime.now()
    print('Time to select 10k random users:', finish-start)


async def main():
    conn_string = f"postgresql://{DB_CONFIG['username']}:{DB_CONFIG['password']}@{DB_CONFIG['host']}/{DB_CONFIG['dbname']}"

    asyncpg_pool = await asyncpg.create_pool(conn_string)

    print('---------------- INDEXED OPERATIONS ----------------')
    await drop_table(asyncpg_pool)
    await create_table(asyncpg_pool)
    await create_index(asyncpg_pool)
    await create_10k_users(asyncpg_pool)
    await select_10k_random_users(asyncpg_pool)

    print('--------------- NON INDEXED OPERATIONS ---------------')
    await drop_table(asyncpg_pool)
    await create_table(asyncpg_pool)
    await create_10k_users(asyncpg_pool)
    await select_10k_random_users(asyncpg_pool)


asyncio.run(main())