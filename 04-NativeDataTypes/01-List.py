Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a = [1,2,3,'Hi',10.5,True,'Bye']
>>> type(a)
<class 'list'>
>>> x = 12
>>> type(x)
<class 'int'>
>>> type(int)
<class 'type'>
>>> type(type)
<class 'type'>
>>> type(None)
<class 'NoneType'>
>>> isinstance(x, int)
True
>>> isinstance(a, int)
False
>>> isinstance(a, list)
True
>>> a[0]
1
>>> a[3]
'Hi'
>>> a[5]
True
>>> a[-1]
'Bye'
>>> a[-2]
True
>>> a[0:4]
[1, 2, 3, 'Hi']
>>> a[0:4:2]
[1, 3]
>>> a[::-1]
['Bye', True, 10.5, 'Hi', 3, 2, 1]
>>> a[0] = 'Python'
>>> a
['Python', 2, 3, 'Hi', 10.5, True, 'Bye']
>>> x = 'Hello'
>>> x[0] = 'Y'
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    x[0] = 'Y'
TypeError: 'str' object does not support item assignment
>>> x[0]
'H'
>>> x.replace('H', 'Y')
'Yello'
>>> x
'Hello'
>>> list_1 = []
>>> list_1.append('Hi')
>>> list_1
['Hi']
>>> list_1.append('Hello')
>>> list_1
['Hi', 'Hello']
>>> list_1.append('Bye')
>>> 
>>> list_1
['Hi', 'Hello', 'Bye']
>>> list_1.append(12,34,56,78,89)
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    list_1.append(12,34,56,78,89)
TypeError: append() takes exactly one argument (5 given)
>>> list_1.append([12,34,56,78,89])
>>> list_1
['Hi', 'Hello', 'Bye', [12, 34, 56, 78, 89]]
>>> list_1.append(100)
>>> list_1
['Hi', 'Hello', 'Bye', [12, 34, 56, 78, 89], 100]
>>> list_1.pop()
100
>>> list_1
['Hi', 'Hello', 'Bye', [12, 34, 56, 78, 89]]
>>> list_1[3]
[12, 34, 56, 78, 89]
>>> list_1[3][4]
89
>>> list_1[3].pop()
89
>>> list_1
['Hi', 'Hello', 'Bye', [12, 34, 56, 78]]
>>> list_1.extend(['Python','Programming'])
>>> list_1
['Hi', 'Hello', 'Bye', [12, 34, 56, 78], 'Python', 'Programming']
>>> list_1.pop(1)
'Hello'
>>> list_1
['Hi', 'Bye', [12, 34, 56, 78], 'Python', 'Programming']
>>> list_1[2].pop(0)
12
>>> list_1
['Hi', 'Bye', [34, 56, 78], 'Python', 'Programming']
>>> list_1.insert(0,'Py')
>>> list_1
['Py', 'Hi', 'Bye', [34, 56, 78], 'Python', 'Programming']
>>> list_1.insert(2,100)
>>> list_1
['Py', 'Hi', 100, 'Bye', [34, 56, 78], 'Python', 'Programming']
>>> list_1[4].append(99)
>>> list_1
['Py', 'Hi', 100, 'Bye', [34, 56, 78, 99], 'Python', 'Programming']
>>> list_1.remove(1)
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    list_1.remove(1)
ValueError: list.remove(x): x not in list
>>> list_1.remove('Hi')
>>> list_1
['Py', 100, 'Bye', [34, 56, 78, 99], 'Python', 'Programming']
>>> list_1.append('Bye')
>>> list_1.remove('Bye')
>>> list_1
['Py', 100, [34, 56, 78, 99], 'Python', 'Programming', 'Bye']
>>> list_1.index('Bye')
5
>>> list_1.reverse()
>>> list_1
['Bye', 'Programming', 'Python', [34, 56, 78, 99], 100, 'Py']
>>> list_1 = [12,45,78,11,23,32,60,1,3]
>>> sorted(list_1)
[1, 3, 11, 12, 23, 32, 45, 60, 78]
>>> list_1
[12, 45, 78, 11, 23, 32, 60, 1, 3]
>>> list_1.sort()
>>> list_1
[1, 3, 11, 12, 23, 32, 45, 60, 78]
>>> list_1.sort(reverse = True)
>>> list_1
[78, 60, 45, 32, 23, 12, 11, 3, 1]
>>> 32 in list_1
True
>>> list_1 = [12,45,78,11,23,[32,60,1,3]]
>>> list_1
[12, 45, 78, 11, 23, [32, 60, 1, 3]]
>>> 32 in list_1
False
>>> 
