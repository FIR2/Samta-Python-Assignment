import mysql.connector

# Connect to the MySQL database
db = mysql.connector.connect(
    host="localhost",       #  MySQL server host name
    user="root",   # MySQL username
    password="Firoz@123",   #MySQL password
    
)

# Create a cursor to interact with the database
cursor = db.cursor()

# Create a database 
cursor.execute("CREATE DATABASE SamtaTech")
