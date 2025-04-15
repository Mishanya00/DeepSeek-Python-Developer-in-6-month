import asyncio
import asyncpg

from datetime import datetime

# I've already connected PostgreSQL to python previous week
# so this time I will try to use asyncpg instead of psycopg


async def main():
    # database.ini stores password for postgres user
    with open("database.ini", encoding="utf-8") as f:
        my_password = f.read()

    conn = await asyncpg.connect(
        f"postgresql://postgres:{my_password}@localhost/temporary"
    )

    today = datetime.now()

    try:
        await conn.execute(
            """
                CREATE TABLE users (
                        id SERIAL PRIMARY KEY,
                        name TEXT,
                        signup_date DATE
                        )
                        """
        )
    except asyncpg.exceptions.DuplicateTableError:
        print('Table "users" has already been created!')
    except Exception as e:
        print(f"Error: {e}")

    try:
        await conn.execute(f"""
                INSERT INTO users(name, signup_date)
                VALUES ( 'Alex Johnes', '{datetime.strftime(today, '%Y-%m-%d')}' ),
                       ( 'Michael Jackson', '{datetime.strftime(today, '%Y-%m-%d')}' ),
                       ( 'Czar Leonid', '{datetime.strftime(today, '%Y-%m-%d')}' )
            """)
    except Exception as e:
        print(f"Error: {e}")

    await conn.close()


asyncio.run(main())
