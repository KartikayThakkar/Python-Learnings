Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def calc(x,y):
	return x + y

>>> calc(2,5)
7
>>> def calc(x,y):
	return x + y, x-y, x/y, x*y

>>> calc(3,7)
(10, -4, 0.42857142857142855, 21)
>>> x = calc(3,7)
>>> x
(10, -4, 0.42857142857142855, 21)
>>> a,b,c,d = calc(5,6)
>>> a
11
>>> b
-1
>>> c
0.8333333333333334
>>> d
30
>>> a,b,c = calc(5,6)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    a,b,c = calc(5,6)
ValueError: too many values to unpack (expected 3)
>>> a,b,*c = calc(5,6)
>>> a
11
>>> b
-1
>>> c
[0.8333333333333334, 30]
>>> a,*b,c = calc(5,6)
>>> a
11
>>> b
[-1, 0.8333333333333334]
>>> c
30
>>> def calc(x,y):
	return x + y
	print("Hello")

	
>>> calc(4,8)
12
>>> def calc(x,y):
	yield x + y
	yield x - y
	yield x / y
	yield x * y

	
>>> calc(5,9)
<generator object calc at 0x00000221C99E6990>
>>> x = calc(5,9)
>>> x
<generator object calc at 0x00000221C9A11048>
>>> for i in x:
	print(i)

	
14
-4
0.5555555555555556
45
>>> next(calc(5,9))
14
>>> next(calc(5,9))
14
>>> next(calc(5,9))
14
>>> for i in range(4):
	print(next(calc(5,9)))

	
14
14
14
14
>>> for i in x:
	print(i)

	
>>> x
<generator object calc at 0x00000221C9A11048>
>>> for i in x:
	print(i)

	
>>> x()
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    x()
TypeError: 'generator' object is not callable
>>> x
<generator object calc at 0x00000221C9A11048>
>>> def calc(x,y):
	yield x + y
	yield x - y
	yield x / y
	yield x * y

	
>>> a = calc(5,9)
>>> for i in a:
	print(i)

	
14
-4
0.5555555555555556
45
>>> 
