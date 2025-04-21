import asyncio
import asyncpg

from pprint import pprint

from config import DB_CONFIG


async def create_books_table(pool: asyncpg.Pool):
    async with pool.acquire() as aconn:
        await aconn.execute(
            """
            CREATE TABLE IF NOT EXISTS books (
                id SERIAL PRIMARY KEY,
                title TEXT UNIQUE NOT NULL,
                author TEXT,
                genre TEXT,
                price DECIMAL(8,2)
            )
            """
        )


async def insert_books(pool: asyncpg.Pool):
    async with pool.acquire() as aconn:
        await aconn.execute(
            """
            DELETE FROM books;
            INSERT INTO books (title, author, genre, price) VALUES
            ('War and Peace', 'Lev Tolstoy', 'Historical Fiction', 19.99),
            ('Anna Karenina', 'Lev Tolstoy', 'Literary Fiction', 14.50),
            ('Crime and Punishment', 'Fyodor Dostoevsky', 'Psychological Fiction', 12.75),
            ('The Brothers Karamazov', 'Fyodor Dostoevsky', 'Philosophical Fiction', 16.20),
            ('The Master and Margarita', 'Mikhail Bulgakov', 'Fantasy', 18.30),
            ('The Idiot', 'Fyodor Dostoevsky', 'Literary Fiction', 15.00),
            ('The Cherry Orchard', 'Anton Chekhov', 'Drama', 11.25),
            ('The Seagull', 'Anton Chekhov', 'Drama', 13.80),
            ('A Hero of Our Time', 'Mikhail Lermontov', 'Adventure', 17.40),
            ('The War of the Worlds', 'H.G. Wells', 'Science Fiction', 10.99),
            ('1984', 'George Orwell', 'Dystopian', 9.99),
            ('Brave New World', 'Aldous Huxley', 'Dystopian', 13.50),
            ('Fahrenheit 451', 'Ray Bradbury', 'Dystopian', 11.00),
            ('Pride and Prejudice', 'Jane Austen', 'Romance', 8.75),
            ('Wuthering Heights', 'Emily Brontë', 'Romance', 12.00),
            ('The Catcher in the Rye', 'J.D. Salinger', 'Literary Fiction', 14.99),
            ('To Kill a Mockingbird', 'Harper Lee', 'Literary Fiction', 15.50),
            ('The Great Gatsby', 'F. Scott Fitzgerald', 'Literary Fiction', 10.50),
            ('Moby Dick', 'Herman Melville', 'Adventure', 16.75),
            ('The Hobbit', 'J.R.R. Tolkien', 'Fantasy', 18.00);
            """
        )


async def group_by_author_books_count(pool: asyncpg.Pool):
    async with pool.acquire() as aconn:
        result = await aconn.fetch("""
            SELECT 
                author, COUNT(title) AS books_count
            FROM books
            GROUP BY author
        """)
        return result


async def avg_prive_by_genre(pool: asyncpg.Pool):
    async with pool.acquire() as aconn:
        result = await aconn.fetch("""
            SELECT 
                genre, SUM(price) / COUNT(title) AS avg_price
            FROM books
            GROUP BY genre
            ORDER BY avg_price DESC
        """)
        return result


async def genres_with_more_3_books(pool: asyncpg.Pool):
    async with pool.acquire() as aconn:
        result = await aconn.fetch("""
            SELECT 
                genre
            FROM books
            GROUP BY genre
            HAVING COUNT(title) > 3
        """)
        return result

async def main():
    conn_string = f"postgresql://{DB_CONFIG['username']}:{DB_CONFIG['password']}@{DB_CONFIG['host']}/{DB_CONFIG['dbname']}"

    connection_pool = await asyncpg.create_pool(conn_string)

    await create_books_table(connection_pool)

    await insert_books(connection_pool)

    first = await group_by_author_books_count(connection_pool)
    second = await avg_prive_by_genre(connection_pool)
    third = await genres_with_more_3_books(connection_pool)
    
    print('--------------- AUTHOR : BOOKS count ---------------')
    for k,v in first:
        print(k, ':', v)
    print('--------------- GENRE : AVERAGE PRICE ---------------')
    for k, v in second:
        print(k, ':', round(v, 2))
    print('--------------- GENRES WITH >3 BOOKS ---------------')   
    for genre in third:
        print(genre)

asyncio.run(main())
