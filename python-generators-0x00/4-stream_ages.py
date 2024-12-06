seed = __import__('seed')

def stream_user_ages():
    """
    Generator that yields user ages one by one from the user_data table.
    """
    conn = seed.connect_to_prodev()
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT age FROM user_data")
            for (age,) in cursor:  # Loop to fetch and yield one age at a time
                yield age
    except Exception as e:
        raise Exception("Error streaming user ages.") from e
    finally:
        conn.close()


total_age = 0
count = 0

for age in stream_user_ages():  
    total_age += age
    count += 1

if count == 0:
    print("No users in the database.")
else:
    average_age = total_age / count
    print(f"Average age of users: {average_age:.2f}")

