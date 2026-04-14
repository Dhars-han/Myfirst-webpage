import mysql.connector

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="your_password_here",  # change this later
        database="student_db"
    )
