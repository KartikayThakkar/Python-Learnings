Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def hello():
	print("Hello")

	
>>> hello
<function hello at 0x0000018CCE78C6A8>
>>> hello()
Hello
>>> print(hello)
<function hello at 0x0000018CCE78C6A8>
>>> print(hello())
Hello
None
>>> x = hello()
Hello
>>> x
>>> cx
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    cx
NameError: name 'cx' is not defined
>>> x
>>> x
>>> type(x)
<class 'NoneType'>
>>> x = hello
>>> x
<function hello at 0x0000018CCE78C6A8>
>>> x()
Hello
>>> type(x)
<class 'function'>
>>> def hello():
	print("Hello")
	return "python"

>>> hello()
Hello
'python'
>>> x = hello
>>> type(x)
<class 'function'>
>>> x = hello()
Hello
>>> def hello():
	return "python"

>>> x = hello()
>>> x
'python'
>>> type(x)
<class 'str'>
>>> def hello():
	return 5

>>> x = hello()
>>> x
5
>>> 
