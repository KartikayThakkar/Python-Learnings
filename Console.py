Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a = 10
>>> b=  0
>>> a/b
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    a/b
ZeroDivisionError: division by zero
>>> a = [{'id':104,'name':'Ram'}, {'id':106, 'name':'Shyam'},{'id':102, 'name' : 'Amit'}]
>>> sorted(a)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    sorted(a)
TypeError: '<' not supported between instances of 'dict' and 'dict'
>>> sorted(a['id'])
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    sorted(a['id'])
TypeError: list indices must be integers or slices, not str
>>> sorted(a[0]['id'])
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    sorted(a[0]['id'])
TypeError: 'int' object is not iterable
>>> sorted(a, key='id')
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    sorted(a, key='id')
TypeError: 'str' object is not callable
>>> def sort_val(x):
	return x['id']

>>> sorted(a, key=sort_val)
[{'id': 102, 'name': 'Amit'}, {'id': 104, 'name': 'Ram'}, {'id': 106, 'name': 'Shyam'}]
>>> def sort_val(x):
	print(x)
	return x['id']

>>> sorted(a, key=sort_val)
{'id': 104, 'name': 'Ram'}
{'id': 106, 'name': 'Shyam'}
{'id': 102, 'name': 'Amit'}
[{'id': 102, 'name': 'Amit'}, {'id': 104, 'name': 'Ram'}, {'id': 106, 'name': 'Shyam'}]
>>> def sort_val(x):
	print(x['id'])
	return x['id']

>>> sorted(a, key=sort_val)
104
106
102
[{'id': 102, 'name': 'Amit'}, {'id': 104, 'name': 'Ram'}, {'id': 106, 'name': 'Shyam'}]
>>> a = [{'id':104,'name':'Ram', 'rno':105}, {'id':106, 'name':'Shyam','rno':102},{'id':102, 'name' : 'Amit','rno':104}]
>>> sorted(a, key=sort_val)
104
106
102
[{'id': 102, 'name': 'Amit', 'rno': 104}, {'id': 104, 'name': 'Ram', 'rno': 105}, {'id': 106, 'name': 'Shyam', 'rno': 102}]
>>> def sort_val(x):
	return x['rno']

>>> sorted(a, key=sort_val)
[{'id': 106, 'name': 'Shyam', 'rno': 102}, {'id': 102, 'name': 'Amit', 'rno': 104}, {'id': 104, 'name': 'Ram', 'rno': 105}]
>>> sorted(a, key=lambda x: x['id'])
[{'id': 102, 'name': 'Amit', 'rno': 104}, {'id': 104, 'name': 'Ram', 'rno': 105}, {'id': 106, 'name': 'Shyam', 'rno': 102}]
>>> def calc(x,y):
	return x+y, x-y, x/y

>>> calc(10,12)
(22, -2, 0.8333333333333334)
>>> def calc(x,y):
	return x+y, x-y, x/y
	print("Hello")

	
>>> calc(10,2)
(12, 8, 5.0)
>>> def calc(x,y):
	yield x+y
	yield x-y
	print("Hello")

	
>>> calc(10,2)
<generator object calc at 0x000002528AB52200>
>>> for d in calc(10,2)"
SyntaxError: EOL while scanning string literal
>>> for d in calc(10,2):
	print(d)

	
12
8
Hello
>>> def calc(x,y):
	if x>y:
		yield x+y
	else:
		yield x-y
	print("Hello")

	
>>> for d in calc(10,12):
	print(d)

	
-2
Hello
>>> def func_1():
	print("This is function_1")

	
>>> def func_2():
	print("This is function_2")

	
>>> def calc(x,y):
	if x>y:
		yield func_2
	else:
		yield func_1
	print("Hello")

	
>>> for d in calc(10,12):
	print(d)

	
<function func_1 at 0x000002528AB32B70>
Hello
>>> for d in calc(10,12):
	print(d())

	
This is function_1
None
Hello
>>> for d in calc(10,12):
	d()

	
This is function_1
Hello
>>> 
