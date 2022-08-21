import csv


with open('2019.csv', 'r', encoding='UTF8') as file:
    csv_reader = list(csv.DictReader(file))
    
results = []
for entry in csv_reader:
    results.append([entry['GDP per capital'], entry['Overall rank'], entry['Country or region']])

results.sort(reverse=True)

cnt = 0
while cnt < 10:
    print(results[cnt][2], results[cnt][0])
    cnt += 1
