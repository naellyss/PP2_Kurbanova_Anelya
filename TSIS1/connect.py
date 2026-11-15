import psycopg2
from config import load_config

def connect():
    try:
        config = load_config()
        conn = psycopg2.connect(**config)
        return conn
    except (psycopg2.DatabaseError, Exception) as error:
        print("Connection error:", error)
        return None

if __name__ == "__main__":
    conn = connect()
    if conn is not None:
        print("Connected to PostgreSQL successfully.")
        conn.close()
