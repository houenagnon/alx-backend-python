seed = __import__('seed')

def stream_users_in_batches(batch_size):
    """
    Generator function to fetch rows in batches from the user_data table.
    
    :param batch_size: Number of rows to fetch in each batch.
    :yield: A batch of rows from the database.
    """
    conn = seed.connect_to_prodev()
    try:
        with conn.cursor() as cursor:
            offset = 0
            while True:
                # Fetch a batch of rows using LIMIT and OFFSET
                cursor.execute("SELECT * FROM user_data LIMIT %s OFFSET %s", (batch_size, offset))
                rows = cursor.fetchall()
                
                if not rows:  # Stop iteration if no more rows
                    break
                
                yield rows
                offset += batch_size
    except Exception as e:
        raise Exception("Error streaming users in batches.") from e
    finally:
        conn.close()


def batch_processing(batch_size):
    """
    Process each batch of users to filter and display users over the age of 25.
    
    :param batch_size: Number of rows to fetch in each batch.
    """
    try:
        for batch in stream_users_in_batches(batch_size):  # Loop 1
            for row in batch:  # Loop 2
                if row[3] > 25:  
                    user_info = {
                        "user_id": row[0],
                        "name": row[1],
                        "email": row[2],
                        "age": row[3]
                    }
                    print(user_info)
    except Exception as e:
        print(f"An error occurred during batch processing: {e}")


