import pandas as pd

df = pd.read_csv('csv_files//2019.csv', skiprows=1)
# df = pd.read_csv('csv_files//2019.csv', delimiter=',')
pd.set_option('display.max_columns', 9)  # Will set option on how many columns to show
pd.set_option('display.max_rows', 156)  # WIll set option on hpw many rows to show
print(df)

print(df.head())  # .head() method will return only head (first 5 rows) of the data frame
print(df.head(3))  # .head() can take arguments into () how many rows to show
print(df.tail())  # .tail() method prints last rows
print(df.tail(3))

# Pure Python example
# Python dictionary
people = {
    "first": ['Bob', 'Alex', 'John', 'Mary'],
    "last": ['Smith', 'Green', 'Black', 'Gold'],
    "email": ['bob@example.com', 'alex@example.com', "john@example.com", 'mary@example.com']
}
print(people['email'])

# Converting python dictionary to data frame
df = pd.DataFrame(people)
print(df)

# Getting values by column
print(df['email'])  # better to use this way
print(df.email)  # same as df['email']
print(type(df['email']))  # Series object
print(df['email'][1:3])
print(df[['first', 'last']])
emails = df.email
for email in emails:
    print(email)

# Series object is iterable
for email in df['email']:
    print(email)

# Several columns can be called. A list needs to be passed into []
print(df[['last', 'email']])
print(type(df[['last', 'email']]))  # Not series anymore. It is data frame

# Working with rows
print(df.iloc[0])  # Will print the first row

# Rows are also iterable
for item in df.iloc[0]:
    print(item)

# Getting several rows
print(df.iloc[[0, 3, 2]])
print(df.iloc[0:3])

# Getting specified columns from several rows
print(df.iloc[[0, 1, 2], [0, 1]])

# Selecting rows with loc instead of iloc will allows to pass column names instead of indexes
print(df.loc[[0, 2], 'email'])
print(df.loc[[0, 1], ['last', 'first']])  # Will return columns in order specified between []

# Shape method returns number of rows and columns in df
df = pd.read_csv('csv_files//2019.csv')
print(df.shape)

# Will count value occurence
print(df['Country or region'].value_counts())

# Selecting specific row and column
print(df.loc[3, 'Country or region'])

# Several rows of one column. Wrap in [] if you have list of indexes
print(df.loc[[1, 2, 3, 4, 50], 'Country or region'])

# Several rows of one column. Don't wrap in [] if you have range of indexes
print(df.loc[1:50, 'Country or region'])

# Column names can be sliced too
print(df.loc[1:50, 'Country or region':'Social support'])

# Each cell can be accessed separately
data = df.loc[2]
print(data['Country or region'] + ' ' + data['Social support'])