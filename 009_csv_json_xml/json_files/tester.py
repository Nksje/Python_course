import json

with open('app.json', 'r', encoding='utf8') as file:
    data = json.load(file)
    # print(data)

for person in data['people']:
    print(f'Hello {person["name"]}. Is {person["name"]} your phone number?')