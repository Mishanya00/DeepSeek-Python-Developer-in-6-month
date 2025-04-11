import psycopg
from config import load_config


def connect(config):
    """Connecting to PostgreSQL database server"""
    try:
        with psycopg.connect(**config) as conn:
            print("Connected to SQL Server")
            return conn
    except (psycopg.DatabaseError, Exception) as error:
        print(error)


if __name__ == "__main__":
    config = load_config()
    connect(config)