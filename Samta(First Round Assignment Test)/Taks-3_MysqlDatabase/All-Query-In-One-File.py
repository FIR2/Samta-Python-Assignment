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

# Create a database 
cursor.execute("CREATE DATABASE SamtaTech")


# ---- create table -- 
cursor.execute ("CREATE TABLE students (student_id INT AUTO_INCREMENT PRIMARY KEY,first_name VARCHAR(255),last_name VARCHAR(255),age INT,grade FLOAT)")



# --------insert value into students ---- 
sql = "INSERT INTO students (student_id,first_name,last_name,age,grade) VALUES (%s,%s,%s,%s,%s)"
val =(1,"Alice", "Smith", 18, 90.5)
    # (2,"Mogra", "Ikash", 19, 95.5),
    # (3,"Dani", "poli", 21, 91), 

cursor.execute(sql, val)
db.commit()


# ----- update table ----
sql = "UPDATE students SET grade = 97.0 WHERE first_name = 'Alice'"
cursor.execute(sql)
db.commit()


# ------ delete specific row =-----
sql = "DELETE FROM students WHERE last_name = 'Smith' "
cursor.execute(sql)
db.commit()


# fatch and display table ---- 
cursor.execute("SELECT * FROM students")
myresult = cursor.fetchall()
for x in myresult:
  print(x)

#   db.close()