import mysql.connector
import pandas as pd

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="12345678",
    database="testdb"
)

mycursor = mydb.cursor()

# # Selecting all data in table
# mycursor.execute("SELECT * FROM students")

# # Add all data to a variable
# myresult = mycursor.fetchall()
#
# for row in myresult:
#     print(row)

# # Fetch only one row of data from database
# myresult = mycursor.fetchone()
# print(myresult)
# for row in myresult:
#     print(row)


# # Using formatted string
# sqlFormula = "SELECT * FROM students WHERE name = %s"
# mycursor.execute(sqlFormula, ("Mary",))
#
# myresult = mycursor.fetchall()
#
# for result in myresult:
#     print(result)
