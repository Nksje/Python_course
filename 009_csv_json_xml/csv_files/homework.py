import csv


with open('2019.csv', 'r', encoding='utf8') as file:
    csv_reader = csv.DictReader(file)
    list1 = list(csv_reader)
    print('Freedom to make life choices')
    for i in list1[0:11]:
        list2 = i['Freedom to make life choices']
        print(list2)

