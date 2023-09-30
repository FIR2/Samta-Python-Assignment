import mysql.connector

# Connect to the MySQL database
db = mysql.connector.connect(
    host="localhost",       #  MySQL server host name
    user="root",   # MySQL username name
    password="Firoz@123",  #  MySQL password
    database="SamtaTech"  # database name
)

# Create a cursor to interact with the database
cursor = db.cursor()

# ---- create table -- 
cursor.execute ("CREATE TABLE students (student_id INT AUTO_INCREMENT PRIMARY KEY,first_name VARCHAR(255),last_name VARCHAR(255),age INT,grade FLOAT)")


