
import mysql.connector


def get_database_connection():
    connection = mysql.connector.connect(
        host='localhost', 
        user='root', 
        password='Kunal@2026',
        database='student_task_manager',
        auth_plugin='mysql_native_password'
    )
    return connection
