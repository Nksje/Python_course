from math import *
from collections import Counter

# Task 1

# name = input('Enter your name: ')
# lastname = input('Enter your lastname: ')
# age = input('Enter your age: ')
# print(f'Hello, {name} {lastname}. Your age is: {age}')

# Task 2

# a = 5
# b = 7
# c = sqrt(a * a + b * b)
# print(c)

# Task 3

# a, b, c = float(input('Enter A side: ')), float(input('Enter B side: ')),\
#           float(input('Enter C side: '))
# if (c ** 2) == a ** 2 + b ** 2:
#     print('Треугольный прямоугольный')
# else:
#     print('Треугольник непрямоугольный')


# Task 4

# list1 = list(input('Enter a list: '))
# list1.reverse()
# for x in list1:
#     print(x)

# Task 5

# a = (1, 2, 3, 4, 5, 8)
# b = (8, 2, 5)
#
# listA = list(a)
# listB = list(b)
#
# listA.insert(2, listB[0])
# listA.insert(3, listB[1])
# listA.insert(4, listB[2])
# listA = tuple(listA)
# print(listA)


# Task 6
# list1 = [1, 2, 3, 4, 7, 9, 9]
# c = Counter(list1)
# most_common = c.most_common(1)[0][0]
# print(list(str(most_common)))


# Task 7

# sec = 1234565
#
# day = sec // 86400
# sec2 = sec - (day * 86400)
# hour = sec2 // 3600
# sec3 = sec2 - (hour * 3600)
# minutes = sec3 // 60
# seconds = sec3 - (minutes * 60)
# print(day, hour, minutes, seconds, sep=":")
