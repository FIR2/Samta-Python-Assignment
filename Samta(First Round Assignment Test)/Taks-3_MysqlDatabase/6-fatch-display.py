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


# fatch and display table ---- 
cursor.execute("SELECT * FROM students")
myresult = cursor.fetchall()
for x in myresult:
  print(x)

#   db.close()