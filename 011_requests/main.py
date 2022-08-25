import requests, lxml
from bs4 import BeautifulSoup as BS
import re

# from requests.exceptions import HTTPError


# 200 - success
# 300 - redirect
# 400 - client errors
# 500 - server errors

# r = requests.get('https://xkcd.com/353/', timeout=10)
# print(r.text)
# print(r.content)
# print(r.ok)
# print(r.encoding)
# print(r.cookies)
# print(r.headers['Server'])
# print(r.headers['SeRvEr'])

headers = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.97 Mobile "
                  "Safari/537.36"}
url = 'https://gammatest.net/course/python/'
request = requests.get(url)

soup = BS(request.content, 'lxml')
test_link = soup.find('table').tr
# print(test_link.td.find_next_siblings())

# print(soup('a'))
# print(soup.find_all(string=re.compile('Словари')))
# print(soup.find_all(['a', 'table']))
# print(soup.find(re.compile()))


# matches = soup.find_all('article', class_='list-article')
# for match in matches:
#     links = match.find_all('a', class_='list-article__url')
#     for link in links:
#         print(link['href'])
#         print(link.div['aria-label'])
# for x in match:
#     links = x.find_all('a')
#     for link in links:
#         print(link.text)

# for url in ['http://api.github.com', 'http://api.github.com/invalid']:
#     try:
#         response = requests.get(url)
#         response.raise_for_status()
#         x = 1 / 0
#     except HTTPError as http_err:
#         print(f'HTTP error occurred: {http_err}')
#     except Exception as err:
#         print(f'Other error occurred: {err}')
#     else :
#         print('Success')
