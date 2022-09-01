from data import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

url = 'https://www.instagram.com'
driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window()

time.sleep(2)

agree_button = driver.find_element('xpath', '/html/body/div[4]/div/div/button[2]')
agree_button.click()

time.sleep(3)

username_field = driver.find_element('name', 'username')
username_field.send_keys(username)

time.sleep(2)

password_field = driver.find_element('name', 'password')
password_field.send_keys(password)

time.sleep(2)

login_button = driver.find_element('xpath', '//*[@id="loginForm"]/div/div[3]/button/div')
login_button.click()

time.sleep(6)

save_data_button = driver.find_element('xpath', '//*[@id="react-root"]/section/main/div/div/div/div/button')
save_data_button.click()

time.sleep(3)

notif_button = driver.find_element('xpath', '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]')
notif_button.click()

time.sleep(2)

profile_icon = driver.find_element('xpath', '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/nav/div[2]/div/div/div[3]/div/div[6]/div[1]/span/img')
profile_icon.click()

time.sleep(1)

profile_page = driver.find_element('xpath', '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/nav/div[2]/div/div/div[3]/div/div[6]/div[2]/div[2]/div[2]/a[1]/div/div[2]/div/div/div/div')
profile_page.click()

photo = driver.find_element()
# driver.quit()