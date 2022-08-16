import datetime as dt
from datetime import datetime

"""
Под каждым комментарием нужно написать одну функцию/программу
Задание в комментарии
input - параметр который функция получает
output - параметр который функция возвращает
"""

# Write a program that converts given string to datetime object
sample1 = 'Jan 1 2014 2:43PM'
sample2 = '14:20 10/12/22'  # YY/MM/DD
sample3 = 'Tuesday, September 24, 2019'
sample4 = '01.01.1970 - 00:00:01'


# sample1_datetime = datetime.strptime(sample1, '%b %d %Y %I:%M%p')
# sample2_datetime = datetime.strptime(sample2, '%H:%M %y/%m/%d')
# sample3_datetime = datetime.strptime(sample3, '%A, %B %d, %Y')
# sample4_datetime = datetime.strptime(sample4, '%d.%m.%Y - %H:%M:%S')


# Write a program to print yesterdays, today and tomorrow dates
# today = dt.date.today()
# yesterday = today - dt.timedelta(days=1)
# tomorrow = today + dt.timedelta(days=1)


# Write a program to convert given timestamp to dd.mm.yyyy format
# some_day = 1014163200
#
# date = datetime.fromtimestamp(some_day)
# print(date)


# Write a function to subtract 2 weeks from timestamp and return new timestamp
# input: timestamp (float)
# output: timestamp (float)

def substract_two_weeks(timestamp):
    return (datetime.fromtimestamp(timestamp) - dt.timedelta(weeks=2)).timestamp()


print(substract_two_weeks(1014163200))
