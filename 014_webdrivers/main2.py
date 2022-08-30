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
views = driver.find_elements('class name', 'style-scope ytd-grid-renderer')
posts = driver.find_elements('class name', 'style-scope ytd-grid-renderer')

video_list = []
amount_views = []
posted_time = []

for video in videos:
    title = video.find_elements('id', 'video-title')
    for ttl in title:
        video_list.append(ttl.text)

for vw in views:
    view = vw.find_elements('xpath', '//*[@id="metadata-line"]/span[1]')
    for viw in view:
        amount_views.append(viw.text)

for post in posts:
    post_time = post.find_elements('xpath', '//*[@id="metadata-line"]/span[2]')
    for pst in post_time:
        posted_time.append(pst.text)

print(video_list)
print(amount_views)
print(posted_time)
time.sleep(3)

driver.quit()
