import re

# Sample string
text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ]  \  | ( )
example.com
321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
Mr. Jones
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
abc
'''

sentence = 'Start a sentence and then bring it to an end'

emails = '''
CoreyMSchafer@gmail.com
corey.schafer@univercity.edu
corey-321-schafer@my-work.net
'''

urls = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''

pattern = re.compile(r'start', re.I)

matches = pattern.search(sentence)


# matches = pattern.finditer(urls)

# subbed_urls = pattern.sub(r'\2\3', urls)

# print(subbed_urls)


# for match in matches:
#     print(match)

print(matches)


