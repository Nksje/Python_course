import requests, lxml
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 "
                  "Safari/537.36"}


def get_btc_eur_value():
    url = 'https://www.google.com/search?q=btc+to+eur&oq=btc+to+&aqs=chrome.0.0i512l2j69i57j0i512l7.2369j0j7&sourceid' \
          '=chrome&ie=UTF-8 '
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, 'lxml')
    result = soup.find('span', class_='pclqee')
    return float(result.text.encode('utf8').replace(b'\xc2\xa0', b'').replace(b',', b'.').decode('utf-8'))


def main():
    while True:
        user_choice = input('Please choose:\n'
                            '1.EUR to BTC\n'
                            '2.BTC to EUR\n'
                            '0.Exit\n')
        if user_choice == '0':
            print('Goodbye')
            break
        elif user_choice == '1':
            user_amount = float(input('Enter amount: '))
            print(user_amount / get_btc_eur_value())
        elif user_choice == '2':
            user_amount = float(input('Enter amount: '))
            print(user_amount * get_btc_eur_value())
        else:
            print('Choice out of range!')


main()
