import mysql.connector
import pandas as pd

conn = mysql.connector.connect(user='root', password='12341234', host='localhost', port=3306, database='course')

pd.set_option('display.max_columns', 10)  # Will set option on how many columns to show
pd.set_option('display.max_rows', 156)  # WIll set option on hpw many rows to show

# Selects all tables in database
# happiness_data = pd.read_sql_query('SHOW TABLES FROM course', conn)
# print(happiness_data)

# Select all data in happiness2 table
data = pd.read_sql_query('SELECT * FROM happiness2', conn)
# print(data)


new_data = data[data['GDP per capita'] > 1]
print(new_data)
