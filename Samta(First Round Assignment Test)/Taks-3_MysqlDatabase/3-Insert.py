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

# --------insert value into students ---- 
sql = "INSERT INTO students (student_id,first_name,last_name,age,grade) VALUES (%s,%s,%s,%s,%s)"
val =(1,"Alice", "Smith", 18, 90.5)
    # (2,"Mogra", "Ikash", 19, 95.5),
    # (3,"Dani", "poli", 21, 91), 

cursor.execute(sql, val)
db.commit()


