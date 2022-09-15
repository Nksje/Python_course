import mysql.connector

# Documentation
# https://dev.mysql.com/doc/connector-python/en/

# First install mysql connector
# pip install mysql-connector-python


# mysql.connector.connect() requires arguments for DB connection
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="12345678",
    database="testdb"
)

# If executes without error, everything worked
print(mydb)

# Cursor initialisation
mycursor = mydb.cursor()

# # Creating a database from Python
# mycursor.execute("CREATE DATABASE testdb")


# # Get all databases from connection
# mycursor.execute("SHOW DATABASES")
# for db in mycursor:
#     print(db)

# # Create table inside database
# mycursor.execute("CREATE TABLE students (name VARCHAR(255), age INTEGER(10))")

# # Get all tables from database
# mycursor.execute("SHOW TABLES")
# for table in mycursor:
#     print(table)

# # Write data into mysql table
# sqlFormula = "INSERT INTO students (name, age) VALUES (%s, %s)"
# student1 = ("John", 22)
# mycursor.execute(sqlFormula, student1)
# mydb.commit()

# # Add many rows to database
# students_list = [("Jack", 33), ("Bob", 45), ("Jane", 28), ("Mary", 30), ("Rachel", 21)]
# mycursor.executemany(sqlFormula, students_list)
# mydb.commit()