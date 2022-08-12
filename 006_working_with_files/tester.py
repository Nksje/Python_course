# 'r' - read
# 'a' - append
# 'w' - write
# 'x' - create
# 'r+' - write and read

# with open('text_files/lorem.txt', 'r', encoding='UTF-8') as file:
#     print(file.closed)
#     print(file.name)

# print(file.closed)


# with open('text_files/python.jpg', 'rb') as file:
    # data = file.readline()
    # print(data)
    # data2 = file.readline()
    # print(data2)

    # file.seek(0)      # Начинает с индекса

    # data = file.read(1000)
    # data2 = file.read()
    # print(data2)
    # data = file.read()

    # data = file.readline(4)
    # print(data)
    # print(file.readline())

    # data = file.readlines(100)
    # print(len(data))
    # print(len(data[0]))

    # chunk_to_read = 4096
    # data = file.read(chunk_to_read)
    # while len(data) > 0:
    #     print(len(data))
    #     data = file.read(chunk_to_read)

    # data = file.read()
    # print(data)

# with open('text_files/lorem_tester.txt', 'x', encoding='utf8') as file:
#     file.write('Hello world!')

with open('text_files/lorem.txt', 'r+', encoding='utf8') as file:
    data = file.read()
    file.seek(0)
    file.write('Hello world!\n')
    file.write(data)
