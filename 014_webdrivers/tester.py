from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
url = 'https://www.youtube.com/c/visitestoniaofficial/videos'
driver = webdriver.Chrome()
width = driver.get_window_size().get('width')
height = driver.get_window_size().get('height')
print(width)
print(height)
print(driver.get_window_size())
# driver.set_window_size(800, 600)

pos_x = driver.get_window_position().get('x')
pos_y = driver.get_window_position().get('y')
print(pos_x, pos_y)
print(driver.get_window_position())

# driver.get('https://www.gammatest.net')

# link = driver.find_element('link text', 'Rohkem infot')
# link.click()
# time.sleep(5)
# driver.back()
# time.sleep(3)
# driver.forward()
# table_data = driver.find_elements('tag name', 'td')
# for td in table_data:
#     print(td.location)
# time.sleep(3)

