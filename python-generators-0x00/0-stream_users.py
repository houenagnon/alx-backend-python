seed = __import__('seed')

def stream_users():
    """
        Streams rows from an SQL database one by one     
    """
    conn = seed.connect_to_prodev()
    try : 
         with conn.cursor() as cursor:
            cursor.execute("SELECT * from user_data")
            result  = cursor.fetchall()

            for r in result:
                yield r
    
    except Exception as e :
        raise e

    