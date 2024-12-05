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

def transactional(func):
    @functools.wraps(func)
    def wrapper(conn,*args, **kwargs):
        try:
            result = func(conn,*args, **kwargs)
            conn.commit()
        except Exception as e:
            conn.rollback()
            raise e
    return wrapper

@with_db_connection 
@transactional 
def update_user_email(conn, user_id, new_email): 
    cursor = conn.cursor() 
    cursor.execute("UPDATE users SET email = ? WHERE id = ?", (new_email, user_id)) 

#### Update user's email with automatic transaction handling 
update_user_email(user_id=1, new_email='Crawford_Cartwright@hotmail.com')