# people = [('Jack', 'Smith', 30, 'male'), ('Sarah', 'Gold', 25, 'female'),
#           ('Mary', 'Summers', 20, 'female'), ('Bob', 'Dylan', 25, 'male')]

# for person in people:
#     print(f'This is {person[0]} {person[1]}. He is {person[2]} years old.')

# for name, lastname, age, gender in people:
#     print(f'This is {name} {lastname}. He is {age} years old.')

# while True:
#     print("I can't stop!")


# x = 0
# while x < 100:
#     print(x ** 2)
#     x += 1

# distance_to_target = float(input('Please enter distance in km: '))
#
# step = 0.8
# step_cnt = 0
#
# current_position = 0
#
# while current_position < distance_to_target * 1000:
#     print(step_cnt)
#     current_position += step
#     step_cnt += 1


# while True:
#     isikukood = input("Please enter ID: ")
#     if len(isikukood) != 11:
#         if len(isikukood) > 11:
#             print('ID is too long!')
#             continue
#         else:
#             print('ID is too short')
#             continue
#     else:
#         print('Your ID is ' + isikukood)
#         break
#     print('Something')
#
# print('Good bye')

# x = 10
# if x < 100:
#     pass


# for letter in 'we learn python':
#     print(letter)
#     if letter == 'y':
#         break

# while True:
#     try:
#         user_input = input('Please enter ID: ')
#         int(user_input)
#         if len(user_input) != 11:
#             if len(user_input) > 11:
#                 print('ID is too long!')
#             else:
#                 print('ID is too short!')
#             raise Exception
#     except ValueError:
#         print('ERROR')
#         continue
#     except Exception:
#         print('Error length')
#         continue
#     else:
#         print('Your ID is ' + user_input)
#         break
#
# print('Good bye!')

# x = 5
# y = 10
# while x > 0:
#     while y > 0:
#         print(y)
#         y -= 1
#     print(x)
#     x -= 1
