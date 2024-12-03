import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # الاتصال بخادم MySQL
        connection = mysql.connector.connect(
            host="localhost",  # Adjust host if necessary
            user="root",  # اسم مستخدم MySQL
            password="your_password"  # كلمة مرور MySQL الخاصة بك
        )
        
        # التحقق من نجاح الاتصال
        if connection.is_connected():
            cursor = connection.cursor()
            # التأكد من أن قاعدة البيانات لا تُنشأ إلا إذا لم تكن موجودة
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            
            # طباعة رسالة إذا تم إنشاء قاعدة البيانات بنجاح أو إذا كانت موجودة بالفعل
            print("Database 'alx_book_store' created successfully or already exists!")
            
            cursor.close()
        else:
            print("Failed to connect to the database.")
    
    except mysql.connector.Error as e:
        # التعامل مع الأخطاء الخاصة بـ MySQL
        print(f"MySQL Error: {e}")
    
    finally:
        # التأكد من إغلاق الاتصال بشكل صحيح
        if connection.is_connected():
            connection.close()
            print("MySQL connection closed.")

# تشغيل الدالة لإنشاء قاعدة البيانات
create_database()
