import csv

with open('test.csv', 'r', encoding='utf8') as file:
    csv_reader = csv.reader(file)
    header = next(csv_reader)
    list1 = list(csv_reader)
    for line in list1:
        line2 = list(line[2]).copy()
        print(str(line2))

#
#     with open('test_copy.csv', 'w', encoding='utf8') as wfile:
#         csv_writer = csv.writer(wfile, delimiter='.', lineterminator='\n')
#         for x in csv_reader:
#             csv_writer.writerow(x)

# with open('test_copy.csv', 'r', encoding='utf8') as file:
#     csv_reader = csv.reader(file, delimiter='-')
#     for line in csv_reader:
#         print(line)

# with open('test.csv', 'r', encoding='UTF8') as file:
#     csv_reader = csv.DictReader(file)
#     # csv_reader = [{'name': 'Jack', 'town': 'Tallinn', 'dob': '16.03.88'}]
#
#     with open('test_copy.csv', 'w', encoding='UTF8') as wfile:
#         field_names = ['Name', 'Date of birth', 'Town']
#         csv_writer = csv.DictWriter(wfile, fieldnames=field_names, lineterminator='\n')
#         csv_writer.writeheader()
#         for line in csv_reader:
#             csv_writer.writerow(line)
