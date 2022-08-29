import requests
from bs4 import BeautifulSoup

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 '
                  'Safari/537.36 '
}

url = 'https://rus.postimees.ee/#_ga=2.262326860.112360475.1661622575-351714070.1599079255'

r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.content, 'lxml')
list_state = soup.find_all('div', class_='list-article__headline')
for list in list_state:
    print(list.text)