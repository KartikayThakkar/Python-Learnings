def atm(menu):
    user_pin = int(input("Enter your pin : "))

    if user_pin == 1234:
        print("Welcome User")
        return menu
    else:
        print("Wrong PIN")

@atm
def menu():
    print("""
    1. Withdraw
    2. Deposit
    3. Transfer
    4. Balance Enquiry
    5. Exit
    """)
    try:
        amount = 0
        bal = 10000
        user_input = input("Enter your choice : ")
        if user_input == "1":
            amount = int(input("Enter the amount you want to withdraw : "))

            assert(amount < bal), "Not sufficient amount"
            bal -= amount
            print("Remaining balance",bal)

    except AssertionError as err:
        print(err)


menu()