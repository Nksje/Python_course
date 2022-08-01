student = {'name': 'Jack', 'age': 32, 'courses': ['Math', 'Art', 'Programming'], 1: 'integer key', 0.23: 'float key',
           5: 'variable', 'var key': 5, True: 'Hello world',
           'dict_key': {'x': 10, 'y': 20}, 'weight': 64}

print(student.get('job', False))
print(student['name'])
key = 'job'
if student.get(key):
    print(student.get(key))
else:
    print(key, 'not found')
deleted = student.pop('weight')
print(deleted)

student.popitem()  # Удалить последний элемент
print(student)

student.update({'name': 'John', 'age': 50, 'phone': '555-55555'})
print(student)

print(bool([]))

sample = {'one': 1}
print(bool(sample))

for val in student:
    print(val, student[val])

print(list(student.keys()))

print(student.items())
for key, value in student.items():
    print(key, value)

for key in student.keys():
    print(key)

for value in student.values():
    print(value)

student2 = student.copy()
student2['name'] = 'Bob'
student['age'] = 13

print(student)
print(student2)
