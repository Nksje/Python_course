import datetime
import re

import mysql.connector


def get_user_data():
    while True:
        user_name = input('Enter your name: ')
        user_surname = input('Enter your surname: ')
        if user_name.lower() == 'exit' or user_surname.lower() == 'exit':
            print('Good Bye')
            quit()
        if not user_name or not user_surname:
            print('Please enter name and surname! ')
            continue
        break
    while True:
        try:
            year = input('Enter year of birth: ')
            month = input('Enter month of birth: ')
            day = input('Enter day of birth: ')
            if year.lower() == 'exit' or month.lower() == 'exit' or day.lower() == 'exit':
                print('Good Bye')
                quit()
            date_of_birth = datetime.date(int(year), int(month), int(day))
        except ValueError:
            print('Date of birth was not entered correctly, try again!')
            continue
        else:
            break
    while True:
        email = input('Please enter email: ')
        if email.lower() == 'exit':
            print('Good Bye')
            quit()
        email_pattern = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')
        if email_pattern.match(email):
            break
        else:
            print('Not a valid email! Try again!')
            continue
    results = {'name': user_name, 'surname': user_surname, 'dob': date_of_birth, 'email': email}
    return results


def add_to_database(data):
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='G173!ksdNNa295Asdg13',
        database='registered_users'
    )
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO `registered_users`.`users` (`user_name`, `user_surname`, `user_dob`, `user_email`) "
                   f"VALUES ('{data['name']}', '{data['surname']}', '{data['dob']}', '{data['email']}');")
    conn.commit()

add_to_database(get_user_data())


"""
CREATE TABLE `registered_users`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `user_name` VARCHAR(45) NOT NULL,
  `user_surname` VARCHAR(45) NOT NULL,
  `user_dob` DATE NOT NULL,
  `user_email` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`id`));
"""

"""
INSERT INTO `registered_users`.`users` (`user_name`, `user_surname`, `user_dob`, `user_email`) 
VALUES ('{data['name']}', '{data['surname']}', '{data['dob']}', '{data['email']}');
"""