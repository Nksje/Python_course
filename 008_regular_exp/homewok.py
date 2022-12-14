from operator import le
import re

# color = "AliceBlue #F0F8FF, " \
#         "Crimson #DC143C, DarkSeaGreen #8fbc8f"


# pattern = re.compile(r'#[0-9A-Fa-f]{6}')
# matches = pattern.finditer(color)

# for match in matches:
#         print(match)


# test_string = 'Check if there is no + sign after number 2*9-6*5, (3+5)-9*4), (17+12)-27*3, 2345-323232+23432342'
#
# pattern = re.compile(r'(\d+)[^+\d]')
# matches = pattern.finditer(test_string)
#
# for match in matches:
#     print(match.group(1))

# test_string = 'Dinner at 09:00. Lunch is at 37:98. Breakfast is at 24:60. Something else at 23:59. 00:00, 210:323, \
# 24:24'
#
# pattern = re.compile(r'\b([0-1][0-9]|2[0-3]):([0-5][0-9])')
# matches = pattern.finditer(test_string)
#
# for match in matches:
#     print(match)

with open('people.txt', 'r', encoding='UTF-8') as file:
    data = file.read()

    name_pattern = re.compile(r'[A-Z][a-z]+ [A-Z][a-z]+')
    address_pattern = re.compile(r'\d{3} [A-Z0-9][a-z]+ St\., [A-Z][A-Za-z-\' ]+ [A-Z]{2} \d+')

    name_matches = name_pattern.finditer(data)
    addresses_matches = address_pattern.finditer(data)

    
    names = []
    addresses = []

    for name in name_matches:
        if name.group()[-2:] != 'St' and name.group() != 'Vice City' and name.group() != 'South Park':
            names.append(name.group())

    
    for address in addresses_matches:
        addresses.append(address.group())
        # print(address.group())
    
    print(len(names))
    print(len(addresses))


# isikukood = 'My ID is 50102173728, 6023321022, 60103023737'

# pattern = re.compile(r'[3456][0-9]{2}(0[1-9]|1[0-2])(0[1-9]|[1-2][0-9]|3[0-1])\d{4}')
# matches = pattern.finditer(isikukood)

# for match in matches:
#     print(match)
