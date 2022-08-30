from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get('https://www.github.com')

# email_field = driver.find_element('name', 'user_email')

# email_field.is_enabled()
# email_field.is_selected()
# email_field.is_displayed()

# email_field.send_keys('danja_bondar@mail.ru')
# email_field.send_keys(Keys.RETURN)
#
# time.sleep(5)
#
# continue_button = driver.find_element('class name', 'signup-continue-button')
# continue_button.click()
#
# password_field = driver.find_element('id', 'password')
# password_field.send_keys('Drakon17212121')
#
# time.sleep(6)
#
# continue_button = driver.find_element('xpath', '//*[@id="password-container"]/div[2]/button')
# continue_button.click()

# try:
#     element = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located(('id', 'user_email'))
#     )
#     print(element.tag_name)
# except:
#     print('Error')
