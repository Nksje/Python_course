courses = ['History', 'Math', 'Literature', 'Physics', 'Programming', 'Math', 'History']
numbers = [1, 5, 6, 8, 3, 4, 2]
# numbers.sort()
# print(list(enumerate(courses)))
#
# for index, subject in enumerate(courses, start=100):
#     print(subject, index)

# for num in numbers:
#     if num % 2 == 0:
#         print(num, 'Even')
#     else:
#         print(num, 'Odd')


# for num1 in range(10):
#     for num2 in range(10):
#         for num3 in range(10):
#             for num4 in range(10):
#                 print(num1, num2, num3, num4)


for num in range(1, 101):
    if num % 3 == 0:
        print(num, 'FIZZ')
    if num % 5 == 0:
        print(num, 'BUZZ')
    if num % 15 == 0:
        print(num, 'FIZZ BUZZ')

