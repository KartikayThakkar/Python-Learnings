def calc(x,y,opr):
    return eval(x + opr + y)

def errHandler():
    print("Wrong Choice")

while True:
    print("""
    1. Add
    2. Sub
    3. Div
    4. Mul
    """)

    userChoice = input("Enter your choice : ")

    num_1 = input("Enter first number : ")
    num_2 = input("Enter second number : ")

    # Event Binding

    todo = {
        "1" : "+",
        "2" : "-",
        "3" : "/",
        "4" : "*"
        }

    opr = todo.get(userChoice)
    result = calc(num_1, num_2, opr)
    print(result)
