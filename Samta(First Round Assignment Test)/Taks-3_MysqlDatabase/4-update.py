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


# ----- update table ----
sql = "UPDATE students SET grade = 97.0 WHERE first_name = 'Alice'"
cursor.execute(sql)
db.commit()


