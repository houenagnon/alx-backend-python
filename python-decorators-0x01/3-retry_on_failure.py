import time
import sqlite3 
import functools

def with_db_connection(func):
    """Décorateur pour gérer automatiquement la connexion à la base de données."""
    @functools.wraps(func) 
    def wrapper(*args, **kwargs):
        conn = sqlite3.connect('../test.db')
        with conn :
            return func(conn, *args, **kwargs) 
        
    return wrapper

def retry_on_failure(retries, delay):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < retries : 
                try:
                    return func(*args, **kwargs) 
                
                except Exception as e : 
                    attempts += 1
                    if attempts >= retries:
                        time.sleep(delay)
        return wrapper
    return decorator
@with_db_connection
@retry_on_failure(retries=3, delay=1)

def fetch_users_with_retry(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    return cursor.fetchall()

#### attempt to fetch users with automatic retry on failure

users = fetch_users_with_retry()
print(users)