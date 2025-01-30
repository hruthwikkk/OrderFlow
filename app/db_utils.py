import psycopg2

POSTGRES_HOST = 'localhost'
POSTGRES_DB = 'orderflow'
POSTGRES_USER = 'user'
POSTGRES_PASSWORD = 'password'

def get_db_connection():
    try:
        conn = psycopg2.connect(
            host=POSTGRES_HOST,
            database=POSTGRES_DB,
            user=POSTGRES_USER,
            password=POSTGRES_PASSWORD
        )
        return conn
    except Exception as e:
        print(f"Database connection error: {e}")
        return None
