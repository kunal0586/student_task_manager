
import mysql.connector



def get_database_connection():
    connection = mysql.connector.connect(
        host='gateway01.ap-southeast-1.prod.aws.tidbcloud.com', 
        user='XxbCGG5JLegsM59.root', 
        password='37HtCKSbBSYXblK2',
        database='student_task_manager',
        port = 4000 
    )
    return connection


# def get_database_connection():
#     connection = mysql.connector.connect(
#         host='localhost', 
#         user='root', 
#         password='Kunal@2026',
#         database='student_task_manager',
#         auth_plugin='mysql_native_password'
#     )
#     return connection
