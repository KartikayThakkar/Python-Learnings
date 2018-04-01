Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def add():
	print("Addition")

	
>>> def sub():
	print("Subtraction")

	
>>> todo = {"1" : add(), "2" : sub()}
Addition
Subtraction
>>> todo = {"1" : add, "2" : sub}
>>> todo.get("1")
<function add at 0x00000246B8CFC6A8>
>>> todo.get("1")()
Addition
>>> result = todo.get("1")
>>> result()
Addition
>>> todo["1"]
<function add at 0x00000246B8CFC6A8>
>>> todo["1"]()
Addition
>>> print("Hello", 12 > 10 if else "Bye")
SyntaxError: invalid syntax
>>> print("Hello", 12 > 10 if, else "Bye")
SyntaxError: invalid syntax
>>> print("Hello", if 12 > 10 else "Bye")
SyntaxError: invalid syntax
>>> print("Hello" if 12 > 10 else "Bye")
Hello
>>> a = 5>4 and 4>3
>>> a
True
>>> a = 10
>>> b = 10
>>> a == b
True
>>> a is b
True
>>> a = [12,13,14]
>>> b = a
>>> a
[12, 13, 14]
>>> b
[12, 13, 14]
>>> a is b
True
>>> a[0] = "Hi"
>>> a is b
True
>>> a
['Hi', 13, 14]
>>> b
['Hi', 13, 14]
>>> a[:]
['Hi', 13, 14]
>>> c = a[:]
>>> a == c
True
>>> a is c
False
>>> a
['Hi', 13, 14]
>>> a[0] = 'bye'
>>> a
['bye', 13, 14]
>>> b
['bye', 13, 14]
>>> c
['Hi', 13, 14]
>>> a
['bye', 13, 14]
>>> a = ['bye', 13, 14,[100,101,102],99,98]
>>> b = a
>>> c = a[:]
>>> id(c)
2502771570888
>>> id(a)
2502771571080
>>> a[0] = 'Hello'
>>> a
['Hello', 13, 14, [100, 101, 102], 99, 98]
>>> b
['Hello', 13, 14, [100, 101, 102], 99, 98]
>>> c
['bye', 13, 14, [100, 101, 102], 99, 98]
>>> a[3][0] = 'Good'
>>> a
['Hello', 13, 14, ['Good', 101, 102], 99, 98]
>>> b
['Hello', 13, 14, ['Good', 101, 102], 99, 98]
>>> c
['bye', 13, 14, ['Good', 101, 102], 99, 98]
>>> import deepcopy
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    import deepcopy
ModuleNotFoundError: No module named 'deepcopy'
>>> import copy
>>> d = copy.deepcopy(a)
>>> a
['Hello', 13, 14, ['Good', 101, 102], 99, 98]
>>> d
['Hello', 13, 14, ['Good', 101, 102], 99, 98]
>>> a[3][0] = "Bad"
>>> a
['Hello', 13, 14, ['Bad', 101, 102], 99, 98]
>>> d
['Hello', 13, 14, ['Good', 101, 102], 99, 98]
>>> 
