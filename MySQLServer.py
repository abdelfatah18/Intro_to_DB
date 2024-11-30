# File: MySQLServer.py

import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Establish the connection to MySQL server
        connection = mysql.connector.connect(
            host='localhost',  # استبدل بـ اسم المضيف الخاص بك إذا كان مختلفًا
            user='root',  # استبدل بـ اسم المستخدم الخاص بك
            password='your_password'  # استبدل بـ كلمة المرور الخاصة بك
        )

        if connection.is_connected():
            cursor = connection.cursor()
            # Create database if it doesn't exist (without using SELECT or SHOW)
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        # Handle any error that occurs during the connection or database creation
        print(f"Error: {e}")
    
    finally:
        # Ensure that the connection is properly closed, whether there is an error or not
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection closed.")

if __name__ == "__main__":
    create_database()
