import time
import sqlite3 
import functools


query_cache = {}

def with_db_connection(func):
    """Décorateur pour gérer automatiquement la connexion à la base de données.""" 
    def wrapper(*args, **kwargs):
        conn = sqlite3.connect('../test.db')
        with conn :
            return func(conn, *args, **kwargs) 
    return wrapper

def cache_query(func):
    @functools.wraps(func)
    def decorator(*args, **kwargs):
        query = kwargs.get('query')

        if not query:
            raise ValueError("The 'query' argument is required")
        if query in query_cache:
            print("Using cached result for query")
            return query_cache[query]
        
        result = func(*args, **kwargs)
        query_cache[query] = result
        print("Query result cached.")
        return result
    return decorator

@with_db_connection
@cache_query
def fetch_users_with_cache(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()

#### First call will cache the result
users = fetch_users_with_cache(query="SELECT * FROM users")

#### Second call will use the cached result
users_again = fetch_users_with_cache(query="SELECT * FROM users")