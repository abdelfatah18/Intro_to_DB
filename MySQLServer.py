import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to the MySQL server
        connection = mysql.connector.connect(
            host="localhost",  # Adjust host if necessary
            user="root",  # Your MySQL username
            password="your_password"  # Your MySQL password
        )
        
        # Check if the connection was successful
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            
            # If the database is created successfully or already exists, print message
            print("Database 'alx_book_store' created successfully or already exists!")
            
            cursor.close()
        else:
            print("Failed to connect to the database.")
    
    except Error as e:
        # Handle any errors (e.g., connection issues)
        print(f"Error: {e}")
    
    finally:
        # Ensure the connection is closed
        if connection.is_connected():
            connection.close()
            print("MySQL connection closed.")

# Run the function to create the database
create_database()
