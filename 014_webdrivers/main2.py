from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

url = 'https://www.youtube.com/c/visitestoniaofficial/videos'
driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window()

agree_button = driver.find_element('xpath', '//*[@id="yDmH0d"]/c-wiz/div/div/div/div[2]/div[1]/div[3]/div[1]/form['
                                            '2]/div/div/button')
agree_button.click()

videos = driver.find_elements('class name', 'style-scope ytd-grid-renderer')

video_list = []

for video in videos:
    title = video.find_elements('id', 'video-title')
    for ttl in title:
        print(ttl.text)

time.sleep(3)

driver.quit()