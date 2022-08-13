with open('trimushketera.txt', 'r', encoding='utf8') as file:
    data = file.read().lower().replace('.', '').replace(',', '').replace('!', '').replace('?', '').split()
    unique_words = list(set(data))
    with open('trimushketera_copy.txt', 'w', encoding='utf8') as result:
        result.write(f'There are {len(data)} words in {file.name}.\n')
        result.write(f'There are {len(unique_words)} unique words in {file.name}.\n')
        unique_words.sort()
        for words in unique_words:
            result.write(words + '\n')

