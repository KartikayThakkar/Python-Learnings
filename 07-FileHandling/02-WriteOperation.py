file = open('helicopter_1.png', 'rb')

data = file.read()

# print(data)

file_1 = open('helicopter_2.png','wb')

file_1.write(data)

file.close()
file_1.close()


