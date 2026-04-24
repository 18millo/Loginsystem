import psycopg2
import os
from dotenv import load_dotenv

# Load variables from .env
load_dotenv()

def get_connection():
    conn = psycopg2.connect(
        dbname = os.getenv("DB_NAME"),
        user = os.getenv("DB_USER"),
        password = os.getenv("DB_PASSWORD"),
        host = os.getenv("DB_HOST"),
        port = os.getenv("DB_PORT")
    )
    return conn

def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id VARCHAR(12) PRIMARY KEY,
            email VARCHAR(255) UNIQUE NOT NULL,
            password TEXT NOT NULL
        );
    """)
    conn.commit()
    cursor.close()
    conn.close()

    print("Tables created successfully ")

if __name__== "__main__":
    create_tables()
