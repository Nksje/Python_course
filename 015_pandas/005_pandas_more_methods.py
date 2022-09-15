import matplotlib.pyplot as plt
import pandas as pd
import re

# More information about python
# https://tproger.ru/digest/data-science-python/#1

df = pd.read_csv('csv_files//2019.csv')

# # iterrows() method will create an iterable object from rows
# for index, row in df.iterrows():
#     print(index, row)
#     print(row['Country or region'])
#

# Print row with condition
print(df.loc[df['Country or region'] == 'Estonia'])

# Description of dataframe
print(df.describe())
print(df.memory_usage(deep=True))

# Sorting by column
print(df.sort_values('Country or region', ascending=True))
print(df.sort_values(['GDP per capita', 'Generosity'], ascending=False))
print(df.sort_values(['Country or region', 'Generosity'], ascending=[1, 0]))

# Sum columns to a new one
df['Total'] = df['GDP per capita'] + df['Generosity'] + df['Perceptions of corruption']
print(df['Total'])
df.insert(loc=3, column="New Column", value=(df['GDP per capita'] * 2))
print(df['New Column'])

# Delete column from dataframe
df = df.drop(columns=['Total'])
print(df)

print(df.dtypes)

# Contains
print(df.loc[df['Country or region'].str.contains('on | an')])

new_df = pd.read_csv('csv_files//test.csv')
print(new_df)

# Select rows with condition
print(df.loc[df['GDP per capita'] < 1, ['Country or region']])

# Group by and find mean
print(df.groupby('GDP per capita').mean().sort_values('Score', ascending=False))

# Group by and sum
print(df.groupby('GDP per capita').sum())


# Group by and count
print(df.groupby('GDP per capita').count())
print(df.groupby('GDP per capita').count()['Score'])


# Largest and smallest value
print('Hello')
print(df.nlargest(5, 'Overall rank'))
print(df.nsmallest(5, 'Overall rank'))


# Concatenate two dataframes
print(pd.concat([df.nlargest(5, 'Overall rank'), df.nsmallest(5, 'Overall rank')]))


# User re pattern to select column names
pattern = re.compile(r'reg', re.I)
print(df.filter(regex=pattern))


# # Working with large data
# for df in pd.read_csv('csv_files//2019.csv', chunksize=5):
#     print('Chunk')
#     print(df)

new_df2 = df[['Country or region', 'GDP per capita']]
new_df2.plot()
plt.show()