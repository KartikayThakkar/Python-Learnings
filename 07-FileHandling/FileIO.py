Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import os
>>> file = open('music_1.ogg', 'rb')
>>> data = file.read()
>>> file_1 = open('music_2.ogg', 'wb')
>>> file_1.write(data)
7079174
>>> file = open('movie_1.mp4', 'rb')
>>> file_1 = open('movie_2.mp4', 'wb')
>>> data = file.read()
>>> file_1.write(data)
2028423535
>>> import shutil
>>> import glob
>>> glob.glob('*.py')
[]
>>> glob.glob('*.mp4')
['dhoni.mp4', 'movie_1.mp4', 'movie_2.mp4']
>>> import os
>>> os.getcwd()
'C:\\Python36'
>>> os.chdir('C:\Users\asus\Music')
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
>>> os.chdir(r'C:\Users\asus\Music')
>>> os.getcwd()
'C:\\Users\\asus\\Music'
>>> glob.glob('*.mp4')
['dhoni.mp4']
>>> glob.glob('*.mp3')
['5-Varlaam Varlaam Vaa-SenSongsMp3.Co.mp3', 'Galti.mp3', 'Na Ja.mp3', 'Shape of You.mp3', 'StreetFighter.mp3']
>>> 
