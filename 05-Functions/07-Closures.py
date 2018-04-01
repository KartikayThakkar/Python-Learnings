# Closures

def outer(x):
    print("This is outer")

    def inner():
        print("This is inner")
        print("Value of x is",x)
        return x + 1

##    print(inner())

    return inner
    
x = outer(10)
print(x())
