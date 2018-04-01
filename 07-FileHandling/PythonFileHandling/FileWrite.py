file = open('file_2.txt', 'w')

# data = 'This is file write operation of python'

data = ['This is file write operation of python\n', 'This data is also written by python']

# file.write(data)

file.writelines(data)

file.close()