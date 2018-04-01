def calc():
    try:
        num_1 = int(input("Enter first number : "))
        num_2 = int(input("Enter second number : "))

        result = num_1 + num_2
        print("Result is",result)

    except ValueError as err:
        # print("There is a error")
        print(err)
        print("Try Again")
        calc()

calc()