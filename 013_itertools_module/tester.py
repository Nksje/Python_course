import itertools


# cnt = itertools.count()

# print(next(cnt))
# print(next(cnt))
# print(next(cnt))
# print(next(cnt))

# data = [100, 200, 300, 400]
# daily_data = itertools.zip_longest(data, range(10), fillvalue=False)
# print(list(daily_data))

# cnt = itertools.count(start=10, step=1)
# cnt = itertools.cycle([1, 2, 3])
# cnt = itertools.repeat(2, 3)


# print(next(cnt))
# print(next(cnt))
# print(next(cnt))
# print(next(cnt))
# print(next(cnt))
# print(next(cnt))
# print(next(cnt))
# print(next(cnt))
# print(next(cnt))

# def squares(x, y):
#     return x ** y


# result = map(squares, range(101))
# print(list(result))

# result2 = itertools.starmap(squares, [[0, 2], [4, 3], [9, 1]])
# print(list(result2))

# result3 = map(squares, range(101), itertools.repeat(2))
# print(list(result3))

# def more_than_two(x):
#     if x > 2:
#         return True
#     return False


# letters = ['a', 'b', 'c', 'd']
# numbers = [0, 1, 2, 3]
# numbers2 = [4, 5, 4, 3, 2, 1, 0, 4]
# names = ['Jack', 'John']

# result = itertools.combinations(range(10), 3)
# for x in result:
#     print(x)

# result2 = itertools.permutations(letters, 2)
# for x in result2:
#     print(x)

# result3 = itertools.product(letters, repeat=2)
# for i in result3:
#     print(i)

# result4 = itertools.combinations_with_replacement(letters, 4)
# for i in result4:
#     print(i)

# combined = itertools.chain(letters, numbers, names)
# print(list(combined.from_iterable(letters)))

# combined = itertools.islice(range(10), 5, 8, 2)
# print(list(combined))

# selectors = [True, False, False, True]
# result = itertools.compress(numbers2, selectors)
# result = itertools.filterfalse(more_than_two, numbers2)
# result = itertools.dropwhile(more_than_two, numbers2)
# print(list(result))

# print(list(filter(more_than_two, numbers2)))
# result2 = itertools.takewhile(more_than_two, numbers2)
# print(list(result2))
# print(list(itertools.accumulate(numbers2)))

people = [
    {
        'name': 'Jack',
        'town': 'Berlin',
    },
    {
        'name': 'Mary',
        'town': 'Berlin',
    },
    {
        'name': 'Taavi',
        'town': 'Berlin',
    },
    {
        'name': 'Pierre',
        'town': 'Tallinn',
    },
    {
        'name': 'Lee',
        'town': 'Tallinn',
    },
    {
        'name': 'Abdul',
        'town': 'Dubai',
    },
    {
        'name': 'Sarah',
        'town': 'Dubai',
    },
    {
        'name': 'Kevin',
        'town': 'Tallinn'
    }
]
people.sort(key=lambda person: person['town'])
result = itertools.groupby(people, lambda person: person['town'])
copy = itertools.tee(result)
# for key, value in result:
#     print(key, list(value))

print(list(copy))