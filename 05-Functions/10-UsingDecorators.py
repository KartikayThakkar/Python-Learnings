def outer(add):
    print("Welcome User")
    pin = input("Enter your PIN: ")
    if pin == "1234":
        print("Welcome Ram")
    else:
        print("Wrong PIN")

    return add


@outer
def caller():
    total_bal = 0
    amount = int(input("Enter amount you want to withdraw : "))
    total_bal += amount

caller()
