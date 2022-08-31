from selenium import webdriver
import time


url = 'https://www.saucedemo.com/'
driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window()

username_finder = driver.find_element('id', 'login_credentials')
username = username_finder.text.replace('Accepted usernames are:', '').split()
username_choice = username[0]

password_finder = driver.find_element('class name', 'login_password')
password = password_finder.text.replace('Password for all users:', '').split()
password = password[0]

username_field = driver.find_element('id', 'user-name')
username_field.send_keys(username_choice)

time.sleep(2)

password_field = driver.find_element('id', 'password')
password_field.send_keys(password)

login_button = driver.find_element('id', 'login-button')
login_button.click()

time.sleep(3)

cart_choice1 = driver.find_element('id', 'add-to-cart-sauce-labs-backpack')
cart_choice2 = driver.find_element('id', 'add-to-cart-sauce-labs-bolt-t-shirt')

cart_choice1.click()
time.sleep(2)
cart_choice2.click()
time.sleep(4)

cart = driver.find_element('class name', 'shopping_cart_link')
cart.click()

time.sleep(2)

checkout_button = driver.find_element('id', 'checkout')
checkout_button.click()

time.sleep(2)

first_name_field = driver.find_element('id', 'first-name')
last_name_field = driver.find_element('id', 'last-name')
zip_code_field = driver.find_element('id', 'postal-code')

first_name_field.send_keys('Daniil')
time.sleep(1)
last_name_field.send_keys('Bondar')
time.sleep(1)
zip_code_field.send_keys('21005')
time.sleep(1)
continue_button = driver.find_element('id', 'continue')
continue_button.click()
time.sleep(2)

finish_button = driver.find_element('id', 'finish')
finish_button.click()
time.sleep(2)

back_home_button = driver.find_element('id', 'back-to-products')
back_home_button.click()
time.sleep(2)

burger_button = driver.find_element('id', 'react-burger-menu-btn')
burger_button.click()
time.sleep(2)

logout_button = driver.find_element('id', 'logout_sidebar_link')
logout_button.click()
time.sleep(3)

driver.quit()