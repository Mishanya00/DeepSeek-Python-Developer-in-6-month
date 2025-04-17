import asyncio
import select
import asyncpg

from config import DB_CONFIG


async def drop_tables(pool: asyncpg.Pool):
    async with pool.acquire() as aconn:
        await aconn.execute("""
            DROP TABLE IF EXISTS users CASCADE;
            DROP TABLE IF EXISTS posts;            
        """)


async def create_users_table(pool: asyncpg.Pool):
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


async def create_posts_table(pool: asyncpg.Pool):
    async with pool.acquire() as aconn:
        await aconn.execute(
            """
                CREATE TABLE IF NOT EXISTS posts (
                        id SERIAL PRIMARY KEY,
                        user_id INT,
                        title TEXT,
                        content TEXT,
                        post_date DATE,
                        CONSTRAINT fk_user
                            FOREIGN KEY(user_id)
                            REFERENCES users(id)
                            ON DELETE CASCADE
                        )
                        """
        )


async def insert_values(pool: asyncpg.Pool):
    async with pool.acquire() as aconn:
        await aconn.execute(""" 
            INSERT INTO users(name) VALUES
            ('Elon Musk'),
            ('Barack Obama'),
            ('Donald J. Trump'),
            ('User1234')
        """)

        await aconn.execute("""
            INSERT INTO posts(user_id, title, content) VALUES
            (1, 'DOGE', 'Department starts its work today'),
            (2, 'USA day', 'Greet you, my citizens!'),
            (3, 'MAGA', 'Mage Amerika Great Again!'),
            (3, 'Singapore', 'Senator, I am singaporean!')
        """)

        await aconn.execute("""
            INSERT INTO posts(title, content) VALUES
            ('Anonymous', 'We are here'),
            ('Anonymous', 'Haha, your DB is HaCkEd!!!')
        """)


async def get_inner_join(pool: asyncpg.Pool):
    async with pool.acquire() as aconn:
        result = await aconn.fetch("""
            SELECT name, title, content FROM users
            INNER JOIN posts ON users.id = posts.user_id
        """) 
        return result
    

async def select_all_posts(pool: asyncpg.Pool):
    async with pool.acquire() as aconn:
        result = await aconn.fetch("""
            SELECT * FROM posts;
        """)
        return result
    

async def get_all_posts_with_author(pool: asyncpg.Pool):
    rows = await get_inner_join(pool)

    for record in rows:
        print(dict(record))


async def get_all_posts(pool: asyncpg.Pool):
    rows = await select_all_posts(pool)

    for record in rows:
        print(dict(record))


async def main():
    conn_string = f"postgresql://{DB_CONFIG['username']}:{DB_CONFIG['password']}@{DB_CONFIG['host']}/{DB_CONFIG['dbname']}"
    
    asyncpg_pool = await asyncpg.create_pool(conn_string)

    await drop_tables(asyncpg_pool)
    await create_users_table(asyncpg_pool)
    await create_posts_table(asyncpg_pool)
    await insert_values(asyncpg_pool)

    print('---------------- ALL POSTS ----------------')
    await get_all_posts(asyncpg_pool)

    print('---------------- ALL POSTS WITH AUTHOR ----------------')
    await get_all_posts_with_author(asyncpg_pool)


asyncio.run(main())