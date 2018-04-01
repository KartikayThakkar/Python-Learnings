Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> list_1 = (1,2,3,4,'Hi', 'hello', 'bye', 100, 99.5)
>>> list_1[4]
'Hi'
>>> list_1[0:8]
(1, 2, 3, 4, 'Hi', 'hello', 'bye', 100)
>>> list_1[0] = 'Bye'
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    list_1[0] = 'Bye'
TypeError: 'tuple' object does not support item assignment
>>> list(list_1)
[1, 2, 3, 4, 'Hi', 'hello', 'bye', 100, 99.5]
>>> dict_1 = {'id' : 101, 'name' : 'Ram', 'age' : 16}
>>> dict_1[0]
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    dict_1[0]
KeyError: 0
>>> dict_1['id']
101
>>> dict_1.keys()
dict_keys(['id', 'name', 'age'])
>>> dict_1.values()
dict_values([101, 'Ram', 16])
>>> dict_1.items()
dict_items([('id', 101), ('name', 'Ram'), ('age', 16)])
>>> for data in dict_1:
	print(data)

	
id
name
age
>>> for data in dict_1.values():
	print(data)

	
101
Ram
16
>>> for data in dict_1.items():
	print(data)

	
('id', 101)
('name', 'Ram')
('age', 16)
>>> dict_1 = {'id' : [101,102,103,104], 'name' : ['Ram','Shyam', 'Mohan', 'Anuj'], 'age' : [16,18,20,21]}
>>> dict_1
{'id': [101, 102, 103, 104], 'name': ['Ram', 'Shyam', 'Mohan', 'Anuj'], 'age': [16, 18, 20, 21]}
>>> dict_1['id']
[101, 102, 103, 104]
>>> dict_1['id'][2]
103
>>> for data in dict_1.items():
	print(data[1])

	
[101, 102, 103, 104]
['Ram', 'Shyam', 'Mohan', 'Anuj']
[16, 18, 20, 21]
>>> for data in dict_1.items():
	print(data)

	
('id', [101, 102, 103, 104])
('name', ['Ram', 'Shyam', 'Mohan', 'Anuj'])
('age', [16, 18, 20, 21])
>>> for data in dict_1.items():
	print(data[0])

	
id
name
age
>>> for data in dict_1.items():
	print(data[0][1])

	
d
a
g
>>> for data in dict_1.items():
	print(data[0], data[1])

	
id [101, 102, 103, 104]
name ['Ram', 'Shyam', 'Mohan', 'Anuj']
age [16, 18, 20, 21]
>>> for data in dict_1.items():
	print(data[0], data[1][0])

	
id 101
name Ram
age 16
>>> i = 0
>>> 
>>> for data in dict_1.items():
	print(data[0], data[1][i])
	i += 1

	
id 101
name Shyam
age 20
>>> for data in dict_1.items():
	for x in data:
		print(x)

		
id
[101, 102, 103, 104]
name
['Ram', 'Shyam', 'Mohan', 'Anuj']
age
[16, 18, 20, 21]
>>> for data in dict_1.items():
	print(data[0], data[1][0])

	
id 101
name Ram
age 16
>>> for data, index in enumerate(dict_1.items()):
	print(data[index], data[1][index])

	
Traceback (most recent call last):
  File "<pyshell#46>", line 2, in <module>
    print(data[index], data[1][index])
TypeError: 'int' object is not subscriptable
>>> for index, data in enumerate(dict_1.items()):
	print(data[index], data[1][index])

	
id 101
['Ram', 'Shyam', 'Mohan', 'Anuj'] Shyam
Traceback (most recent call last):
  File "<pyshell#48>", line 2, in <module>
    print(data[index], data[1][index])
IndexError: tuple index out of range
>>> for data in dict_1.items():
	print(data[1], data[1][1])

	
[101, 102, 103, 104] 102
['Ram', 'Shyam', 'Mohan', 'Anuj'] Shyam
[16, 18, 20, 21] 18
>>> for data in dict_1.items():
	print(data[0], data[1][1])

	
id 102
name Shyam
age 18
>>> for index, data in enumerate(dict_1.items()):
	print(data[0], data[1][index])

	
id 101
name Shyam
age 20
>>> for index, data in enumerate(dict_1.items()):
	print(data[0], data[1][0])

	
id 101
name Ram
age 16
>>> for index, data in enumerate(dict_1.items()):
	print(data[0], data[1][1])

	
id 102
name Shyam
age 18
>>> for index, data in enumerate(dict_1.items()):
	print(data[0], data[1][2])

	
id 103
name Mohan
age 20
>>> for index, data in enumerate(dict_1.items()):
	print(data[0], data[1][index])

	
id 101
name Shyam
age 20
>>> for index, data in enumerate(dict_1.items()):
	print(index)
	print(data[0], data[1][index])

	
0
id 101
1
name Shyam
2
age 20
>>> for data in dict_1.items():
	for i in data:
		print(data[0], data[1][i])

		
Traceback (most recent call last):
  File "<pyshell#67>", line 3, in <module>
    print(data[0], data[1][i])
TypeError: list indices must be integers or slices, not str
>>> for data in dict_1.items():
	for i in data:
		print(data[0], data[1][1])

		
id 102
id 102
name Shyam
name Shyam
age 18
age 18
>>> for data in dict_1.items():
	print(data[0], data[1][0])

	
id 101
name Ram
age 16
>>> i = 0
>>> for data in dict_1.items():
	print(data[0], data[1][i])
	i += 1

	
id 101
name Shyam
age 20
>>> dict_1.items()
dict_items([('id', [101, 102, 103, 104]), ('name', ['Ram', 'Shyam', 'Mohan', 'Anuj']), ('age', [16, 18, 20, 21])])
>>> index = [0,1,2,3]
>>> for data,i in zip(dict_1.items(), index):
	print(data[0], data[1][i])

	
id 101
name Shyam
age 20
>>> for i in range(4):
	for data in dict_1.items():
		print(data[0], data[1][i])

		
id 101
name Ram
age 16
id 102
name Shyam
age 18
id 103
name Mohan
age 20
id 104
name Anuj
age 21
>>> for data in dict_1.items():
	print(data[0], data[1])

	
id [101, 102, 103, 104]
name ['Ram', 'Shyam', 'Mohan', 'Anuj']
age [16, 18, 20, 21]
>>> for data in dict_1.items():
	print(data[0], data[1][0])

	
id 101
name Ram
age 16
>>> for data in dict_1.items():
	print(data[0], data[1][1])

	
id 102
name Shyam
age 18
>>> for data, i in zip(dict_1.items(), index):
	print(i)
	print(data[0], data[1][i])

	
0
id 101
1
name Shyam
2
age 20
>>> for i, data in enumerate(dict_1.items()):
	print(i)

	
0
1
2
>>> for i, data in enumerate(dict_1.items()):
	print(i)
	print(data)

	
0
('id', [101, 102, 103, 104])
1
('name', ['Ram', 'Shyam', 'Mohan', 'Anuj'])
2
('age', [16, 18, 20, 21])
>>> for i, data in enumerate(dict_1.items()):
	print(i, data)

	
0 ('id', [101, 102, 103, 104])
1 ('name', ['Ram', 'Shyam', 'Mohan', 'Anuj'])
2 ('age', [16, 18, 20, 21])
>>> for i, data in enumerate(dict_1.items()):
	print(data[0], data[1],[i])

	
id [101, 102, 103, 104] [0]
name ['Ram', 'Shyam', 'Mohan', 'Anuj'] [1]
age [16, 18, 20, 21] [2]
>>> for i, data in enumerate(dict_1.items()):
	print(data[0], data[1][i])

	
id 101
name Shyam
age 20
>>> 
