import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # محاولة الاتصال بخادم MySQL
        connection = mysql.connector.connect(
            host='localhost',
            user='your_username',  # استبدل باسم المستخدم الخاص بك
            password='your_password'  # استبدل بكلمة المرور الخاصة بك
        )
        
        if connection.is_connected():
            cursor = connection.cursor()
            # استخدام CREATE DATABASE IF NOT EXISTS فقط
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")
    except Error as e:
        # معالجة الأخطاء وطباعة رسالة مفصلة
        print("An error occurred while creating the database:")
        print(e)
    finally:
        # إغلاق الاتصال بعد الانتهاء
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection closed.")

if __name__ == "__main__":
    create_database()
