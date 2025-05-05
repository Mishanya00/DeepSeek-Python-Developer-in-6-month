import sqlite3
from sqlalchemy import create_engine

from config import load_config


DB_CONFIG = load_config()
print(DB_CONFIG)

conn_str = f"""postgresql+asyncpg://{DB_CONFIG["username"]}:{DB_CONFIG["password"]}@{DB_CONFIG["host"]}:5432/{DB_CONFIG["dbname"]}"""

Engine = create_engine(conn_str, echo=True)