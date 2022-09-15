import pandas as pd

# File import is done by pd.read_csv() method. DF stands for Data Frame
df = pd.read_csv('csv_files//2019.csv')
print(df)
print(type(df))


# Sometimes there are 2 headers in csv file, it can be skipped
df = pd.read_csv('csv_files//2019.csv', skiprows=1)
print(df)

# Same result if header=1 added instead of skiprows
df = pd.read_csv('csv_files//2019.csv', header=1)
print(df)

# If there is no header, just put header=None. Column names are generated automatically
df = pd.read_csv('csv_files//test.csv', header=None)
print(df)

# Names of the columns can be added manually
df = pd.read_csv('csv_files//test.csv', header=None, names=['Name', 'Date of birth', 'Hometown'])
print(df)
#
# You can choose number of rows shown (excluding header)
df = pd.read_csv('csv_files//2019.csv', header=1, nrows=5)


# You can save data frames to csv file
df.to_csv('csv_files//new.csv')
df.to_csv('csv_files//new_noindex.csv', index=False)
df.to_csv('csv_files//new_noheader.csv', header=False)

df = pd.read_csv('csv_files//2019.csv', skiprows=1)
print(df.columns)  # columns method gives returns a list of column names from data frame
print(type(df.columns))  # However it doesn't return list item, but pandas specific data type

# Using columns argument if to_csv method, you can choose which columns to write into csv file
df.to_csv('csv_files//csv_columns.csv', columns=['Country or region', 'Freedom to make life choices', 'Score'])

