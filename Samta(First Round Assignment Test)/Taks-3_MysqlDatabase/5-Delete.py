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

# ------ delete specific row =-----
sql = "DELETE FROM students WHERE last_name = 'Smith' "
cursor.execute(sql)
db.commit()

