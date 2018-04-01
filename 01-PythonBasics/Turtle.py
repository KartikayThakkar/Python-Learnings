Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import turtle
>>> turtle.Pen()
<turtle.Turtle object at 0x000002226E133DD8>
>>> turtle.shape('turtle')
>>> turtle.forward(100)
>>> turtle.left(90)
>>> turtle.forward(100)
>>> turtle.left(90)
>>> turtle.forward(100)
>>> turtle.left(90)
>>> turtle.forward(100)
>>> turtle.reset()
>>> for i in range(5):
	turtle.forward(100)
	turtle.left(90)

	
>>> turtle.reset()
>>> for i in range(30):
	turtle.forward(5+i)
	turtle.left(90)

	
>>> turtle.reset()
>>> for i in range(30):
	turtle.forward(2*i)
	turtle.left(90)

	
>>> turtle.reset()
>>> for i in range(30):
	turtle.forward(5*i)
	turtle.left(10*i)

	
>>> turtle.reset()
>>> for i in range(30):
	turtle.circle(5*i)

	
>>> turtle.reset()
>>> for i in range(30):
	turtle.circle(5*i)
	turtle.left(2*i)

	
>>> 
KeyboardInterrupt
>>> turtle.reset()
>>> turtle.speed(0)
>>> for i in range(100):
	turtle.circle(3*i)
	turtle.left(2*i)

	
>>> turtle.reset()
>>> turtle.speed(5)
>>> for i in range(100):
	turtle.circle(3*i)
	turtle.left(2*i)

	
Traceback (most recent call last):
  File "<pyshell#39>", line 2, in <module>
    turtle.circle(3*i)
  File "<string>", line 8, in circle
  File "C:\Python36\lib\turtle.py", line 1991, in circle
    self._go(l)
  File "C:\Python36\lib\turtle.py", line 1605, in _go
    self._goto(ende)
  File "C:\Python36\lib\turtle.py", line 3195, in _goto
    self._update() #count=True)
  File "C:\Python36\lib\turtle.py", line 2663, in _update
    screen._delay(screen._delayvalue) # TurtleScreenBase
  File "C:\Python36\lib\turtle.py", line 566, in _delay
    self.cv.after(delay)
  File "C:\Python36\lib\tkinter\__init__.py", line 741, in after
    self.tk.call('after', ms)
KeyboardInterrupt
>>> 
