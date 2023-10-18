import requests
import lxml
from bs4 import BeautifulSoup
import json
import datetime


def get_weather_data():
    url = 'https://www.ilmateenistus.ee/ilm/ilmavaatlused/vaatlusandmed/oopaevaandmed/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/104.0.0.0 '
                      'Safari/537.36'}

    r = requests.get(url, timeout=10, headers=headers)
    soup = BeautifulSoup(r.content, 'lxml')
    data_rows = soup.tbody.find_all('tr')
    data_names = ['Air temp average', 'Air temp max', 'Air temp min', 'Ground temp', 'Ground temp 2cm', 'Humidity average',
                  'Humidity minimal', 'Air speed average', 'Air speed maximum', 'Chance of rain', 'Sunshine']
    result = {}
    for tr in data_rows:
        key = tr.findChild('td').text
        data = [x.text for x in tr.findChildren('td') if x.text != key]
        full_data = list(zip(data_names, data))
        data_dict = {}
        for entry in full_data:
            data_dict[entry[0]] = entry[1]
        result[key] = data_dict

    return result


def write_data_to_file(data):
    with open('weather.json', 'r') as file:
        data2 = json.load(file)
        if str(datetime.date.today()) not in data2.keys():
            data2[str(datetime.date.today())] = data
            with open('weather.json', 'w') as file:
                json.dump(data2, file, indent=2)
        else:
            print('Data is up to date')


def main():
    pass


write_data_to_file(get_weather_data())
