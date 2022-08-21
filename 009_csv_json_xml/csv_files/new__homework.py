import csv

with open('2019.csv', 'r', encoding='utf8') as file:
    csv_reader = list(csv.DictReader(file))

csv_reader.sort(key=lambda x: x['GDP per capital'], reverse=True)


cnt = 0
results = []
while cnt < 10:
    results.append(csv_reader[cnt])
    cnt += 1

for i in results:
    print(i)

