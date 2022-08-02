# def sum_two_numbers():
#     print(x + y)
#
#
# x = 10
# y = 20
#
# sum_two_numbers()
#
# print(x)


# def no_parameters():
#     x = 25 ** 2
#     return x  # После return действие заканчивается
#
#
# no_parameters()


# def double(number):
#     return number * 2
#
#
# number = 12
#
# print(double(10))

# student = {'name': 'Jack', 'lastname': 'Smith', 'age': 30,
#            'courses': ['Art', 'Math', 'Programming']}
#
#
# def greet_student(data):
#     print(f"Hello {data['name']} {data['lastname']}. You are {data['age']} years old."
#           f"Your subjects are {', '.join(data['courses'])}.")
#
#
# greet_student(student)


# def tester(a, b, *args, **kwargs):       # args = tuple, kwargs = dict
#     print(a, b)
#     print(args)
#     for num in args:
#         print(num ** 2)
#     print(kwargs)
#
#
# tester(10, 32, 100, 5, 5, 77, 7675, 677, name='Daniil', lastname='Bondar')

def perimeter(width, height):
    return (width + height) * 2


def area(width, height):
    return width * height


def count_materials(order):
    result = {}
    for key in order:
        result[key] = [perimeter(order[key][0], order[key][1]) * order[key][2],
                       area(order[key][0], order[key][1]) * order[key][2]]

    return result


def count_total_materials(materials_dict):
    total_p = 0
    total_a = 0
    for key in materials_dict:
        total_p += materials_dict[key][0] / 100
        total_a += materials_dict[key][1] / 1000
    return [total_p, total_a]


carpets = {'small': [60, 60, 15], 'medium': [60, 90, 47], 'large': [90, 90, 20],
           'xlarge': [125, 125, 5]}


def main():
    user_choice = input('1.Material by type\n2.Total material\n-->')
    if user_choice == '1':
        print(count_materials(carpets))
    elif user_choice == '2':
        print(count_total_materials(count_materials(carpets)))
    else:
        quit()


main()
