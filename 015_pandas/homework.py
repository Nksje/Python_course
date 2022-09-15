import pandas as pd

'''
Домашнее задание:
Для опроса на Stack Overflow (https://insights.stackoverflow.com/survey)
Написать программу, которая по выбору пользователя делает следующее:
1. Выводит данные о том сколько программистов является профессионалами и сколько хобби программистами. (столбец 'Hobbyist')
2. Выводит средний, максимальный и минимальный возраст (столбец 'Age') программистов
3. Выводит таблицу со странами (столбец 'Country'). Группирует, считает кол-во и выводит в порядке убывания.
4. Выводит таблицу с валютами (столбец 'CurrencyDesc'). Группирует и выводит в порядке убывания.
'''

# https://tproger.ru/digest/data-science-python/#1

survey_data = pd.read_csv('csv_files/survey_results_public.csv')

# Hobbyist column grouping
print(survey_data.groupby('Hobbyist').count()['Respondent'])
print(survey_data['Hobbyist'].value_counts())

# Max, min and median age
print(f"Maximum age: {survey_data['Age'].max()}")
print(f"Minimum age: {survey_data['Age'].min()}")
print(f"Median age: {survey_data['Age'].mean()}")

# Country stats
print(survey_data['Country'].value_counts(ascending=False))
print(survey_data.groupby('Country').count().sort_values('Respondent', ascending=False)['Respondent'])

# Currency stats
print(survey_data[['CurrencyDesc', 'CurrencySymbol']].value_counts(ascending=False))
print(survey_data.groupby('CurrencyDesc').count().sort_values('Respondent', ascending=False)[ 'Respondent'])
