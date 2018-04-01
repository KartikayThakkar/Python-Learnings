Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import os
>>> os.system('dhoni.mp4')
0
>>> os.system('music_1.ogg')
0
>>> os.startfile('calc')
>>> os.startfile('notepad')
>>> import sys
>>> a = 12
>>> sys.getsizeof(a)
28
>>> from datetime import date
>>> from datetime import time
>>> from datetime import datetime
>>> now = datetime.today()
>>> now
datetime.datetime(2018, 1, 2, 17, 23, 52, 312387)
>>> print(now)
2018-01-02 17:23:52.312387
>>> now = datetime.time()
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    now = datetime.time()
TypeError: descriptor 'time' of 'datetime.datetime' object needs an argument
>>> now = datetime.time
>>> now
<method 'time' of 'datetime.datetime' objects>
>>> now()
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    now()
TypeError: descriptor 'time' of 'datetime.datetime' object needs an argument
>>> now = datetime.time(datetime.now())
>>> now
datetime.time(17, 24, 41, 31699)
>>> print(now)
17:24:41.031699
>>> datetime.strftime('%A')
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    datetime.strftime('%A')
TypeError: descriptor 'strftime' requires a 'datetime.date' object but received a 'str'
>>> now.strftime("%I:%M:%S: %p")
'05:24:41: PM'
>>> now.strftime("%H:%M:%S: %p")
'17:24:41: PM'
>>> now.strftime("%A")
'Monday'
>>> now.strftime("%a")
'Mon'
>>> now.strftime("%d")
'01'
>>> now.strftime("%D")
'01/01/00'
>>> now
datetime.time(17, 24, 41, 31699)
>>> now.strftime("%y")
'00'
>>> now.strftime("%Y")
'1900'
>>> now = datetime.now()
>>> now.strftime("%Y")
'2018'
>>> now.strftime("%D")
'01/02/18'
>>> now.strftime("%a")
'Tue'
>>> import calendar
>>> m = calendar.month(2018, 1)
>>> print(m)
    January 2018
Mo Tu We Th Fr Sa Su
 1  2  3  4  5  6  7
 8  9 10 11 12 13 14
15 16 17 18 19 20 21
22 23 24 25 26 27 28
29 30 31

>>> 
