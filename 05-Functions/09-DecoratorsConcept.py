import datetime

def outer(add):
    print("This is outer function")
    return add

def caller():
    x = 10
    y = 12
    print("Addition is",x+y)

# caller()
a = outer(caller)
a()
