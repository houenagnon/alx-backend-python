import mysql.connector
import csv
import uuid

def connect_db():
    """
    Connects to the MySQL database server.
    """
    try:
        return mysql.connector.connect(
            host="localhost",
            user="user1",
            password=""
        )
    except mysql.connector.Error as e:
        raise Exception("Failed to connect to the MySQL server.") from e


def create_database(connection):
    """
    Creates the database ALX_prodev if it does not exist.
    """
    try:
        with connection.cursor() as cursor:
            cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev")
            print("Database ALX_prodev created or already exists.")
    except mysql.connector.Error as e:
        raise Exception("Failed to create the database ALX_prodev.") from e


def connect_to_prodev():
    """
    Connects to the ALX_prodev database in MySQL.
    """
    try:
        return mysql.connector.connect(
            host="localhost",
            user="user1",
            password="",
            database="ALX_prodev"
        )
    except mysql.connector.Error as e:
        raise Exception("Failed to connect to the ALX_prodev database.") from e


def create_table(connection):
    """
    Creates a table user_data if it does not exist with the required fields.
    """
    try:
        with connection.cursor() as cursor:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS user_data (
                    user_id CHAR(36) PRIMARY KEY NOT NULL,
                    name VARCHAR(255) NOT NULL,
                    email VARCHAR(255) NOT NULL UNIQUE,
                    age INT NOT NULL
                )   
            """)
            print("Table user_data created or already exists.")
    except mysql.connector.Error as e:
        raise Exception("Failed to create the user_data table.") from e


def insert_data(connection, data):
    """
    Inserts data into the user_data table from a CSV file.
    """
    try:
        with connection.cursor() as cursor:
            # Prepare the SQL insert statement
            insert_query = """
                INSERT INTO user_data (user_id, name, email, age)
                VALUES (%s, %s, %s, %s)
            """

            # Open and read the CSV file
            with open(data, mode='r') as file:
                reader = csv.reader(file)
                next(reader)  # Skip the header row

                for row in reader:
                    # Generate a new UUID for each row
                    user_id = str(uuid.uuid4())

                    # Ensure the data matches the expected types
                    if len(row) != 3 or not row[2].isdigit():
                        print(f"Skipping invalid row: {row}")
                        continue

                    # Add user_id to the row and execute the query
                    cursor.execute(insert_query, (user_id, row[0], row[1], int(row[2])))

            connection.commit()  # Commit the transaction
            print("Data successfully inserted into the user_data table.")
    except mysql.connector.Error as e:
        raise Exception("Failed to insert data into the database.") from e
    except FileNotFoundError:
        raise Exception(f"File {data} not found.")
    except Exception as e:
        raise Exception("An unexpected error occurred.") from e




