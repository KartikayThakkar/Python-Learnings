def add(x,y):
    result = x + y
    print("Addition is",result)

def sub(x,y):
    result = x - y if x > y else y - x
    print("Subtraction is",result)

def div():
    pass

def mul():
    pass

while True:
    print("""
    1. Add
    2. Sub
    3. Div
    4. Mul
    """)

    userChoice = input("Enter your choice : ")

    num_1 = int(input("Enter first number : "))
    num_2 = int(input("Enter second number : "))

    # Event Binding

    todo = {
        "1" : add,
        "2" : sub,
        "3" : div,
        "4" : mul
        }

    result = todo.get(userChoice)
    result(num_1,num_2)
