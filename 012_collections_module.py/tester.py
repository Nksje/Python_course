# from collections import Counter, defaultdict, deque, namedtuple, OrderedDict

# Counter

# sample_string = 'aaaaaaaaaaaabbbbbbbbbbcccccccccdddddddddddeeeeeeeeeee'
# my_counter = Counter(sample_string)
# print(my_counter.keys())
# print(my_counter.values())
# print(my_counter.most_common(2))
# print(list(my_counter.elements()))

# Namedtuple

# Point = namedtuple('Point', 'x,y')
# pt = Point(10, 20)
# print(pt.x)

# OrderedDict

# some_dict = {'name': 'Jack', 'surname': 'Smith', 'age': 30}
# ordered = OrderedDict(some_dict)
# print(ordered)

# DefaultDict

# default = defaultdict(bool)
# default['a'] = 'a'
# default['b'] = 'a'
# print(default['c'])

# Deque

# d = deque()
# d.append(1)
# d.append(2)
# d.appendleft(3)
# d.popleft()
# print(d)
# d.extendleft([4, 5, 6])
# d.rotate(-2)
# print(d)