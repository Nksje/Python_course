from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
url = 'https://www.youtube.com/c/visitestoniaofficial/videos'
driver = webdriver.Chrome()
# width = driver.get_window_size().get('width')
# height = driver.get_window_size().get('height')
# print(width)
# print(height)
# print(driver.get_window_size())
# driver.set_window_size(800, 600)
#
# pos_x = driver.get_window_position().get('x')
# pos_y = driver.get_window_position().get('y')
# print(pos_x, pos_y)
# print(driver.get_window_position())

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

# driver.maximize_window()
# time.sleep(3)
# driver.minimize_window()
# time.sleep(3)
# driver.fullscreen_window()

# driver.get(url)
# agree_button = driver.find_element('xpath', '//*[@id="yDmH0d"]/c-wiz/div/div/div/div[2]/div[1]/div[3]/div[1]/form['
#                                             '2]/div/div/button')
# agree_button.click()
#
# element = driver.find_element('id', 'dismissible')
# element.screenshot('element_screenshot.png')
driver.get(url)
agree_button = driver.find_element('xpath', '//*[@id="yDmH0d"]/c-wiz/div/div/div/div[2]/div[1]/div[3]/div[1]/form['
                                            '2]/div/div/button')
agree_button.click()
# print(driver.current_url)
original_window = driver.current_window_handle

driver.switch_to.new_window('tab')
driver.get('https://www.github.com')
second_window = driver.current_window_handle

driver.switch_to.window(original_window)
# driver.quit()
