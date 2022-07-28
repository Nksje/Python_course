# 1 Высчитывает возраст из заданых данных

# years
current_year = 2022
year_of_birth = 1988
age = current_year - year_of_birth  # Возраст

# name
user_name = 'John'
user_surname = 'Smith'

# 2 Найти недостающую часть кода
code_1 = '354'
code_3 = 132
x = 152
y = 132
z = str(int(((x % y) * 13) ** 0.5))
# print(z)  # Недостающая часть кода
# 3 Соединить код в отдельную переменную
secret_code = code_1 + '-' + z + '-' + str(y)

# 4 Вывести строку
print('Hello ' + user_name + ' ' + user_surname + '.' + ' Your secret code is ' + secret_code + '.')
