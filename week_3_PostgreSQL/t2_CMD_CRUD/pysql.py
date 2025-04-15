from argparse import ArgumentParser
from datetime import datetime
import asyncio
import asyncpg

from config import DB_CONFIG


async def select_all(pool: asyncpg.Pool):
    async with pool.acquire() as aconn:
        result = await aconn.fetch('SELECT * FROM users')
        return result
    

async def delete(pool: asyncpg.Pool, id: int):
    async with pool.acquire() as aconn:
        result = await aconn.fetchrow('DELETE FROM users WHERE id = $1 RETURNING *', id)
        return result
    

# Even so asyncpg prevents sql injection via 
# asyncpg.exceptions.PostgresSyntaxError: cannot insert multiple commands into a prepared statement
# result = await aconn.fetchrow(f"INSERT INTO users(name) VALUES ('{name}')")   

async def create_user(pool: asyncpg.Pool, name: str):
    async with pool.acquire() as aconn:
        result = await aconn.fetchrow(f'INSERT INTO users(name, signup_date) VALUES ($1, $2)', name, datetime.now())
        return result


async def list_all_users(pool: asyncpg.Pool):
    records = await select_all(pool)
    for row in records:
        print(f"ID: {row['id']:10} | Name: {row['name']:20} | date: {str(row['signup_date']):16}|")


async def delete_by_id(pool: asyncpg.Pool, id: int):
    record = await delete(pool, id)
    if record:
        print(f'User "{record["name"]}" deleted!')
    else:
        print(f'No user with ID = {id} in the database!')


async def main():
    conn_string = f"postgresql://{DB_CONFIG['username']}:{DB_CONFIG['password']}@{DB_CONFIG['host']}/{DB_CONFIG['dbname']}"

    asyncpg_pool = await asyncpg.create_pool(conn_string)

    parser = ArgumentParser(description="3W.2D task: CLI database tool")
    parser.add_argument('--add', type=str, help='Add new user')
    parser.add_argument('--delete', type=int, help='Delete user by ID')
    parser.add_argument('--list', action='store_true', help='List all users')

    arguments = parser.parse_args()

    
    if arguments.add:
        await create_user(asyncpg_pool, arguments.add)
    if arguments.delete:
        await delete_by_id(asyncpg_pool, arguments.delete)
    if arguments.list:
        await list_all_users(asyncpg_pool)




asyncio.run(main())
