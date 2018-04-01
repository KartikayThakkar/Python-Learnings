def outer(x):
    print("This is outer")
    x()

def inner():
    print("This is inner")

outer(inner)
