def calc():
    try:
        num_1 = int(input("Enter first number : "))
        num_2 = int(input("Enter second number : "))

        addition = num_1 + num_2
        print("Addition is", addition)

        division = num_1 / num_2 if num_1 > num_2 else num_2 / num_1
        print("Division is",division)

        # if division == 0.0:
        #     print(True)

    except (ArithmeticError, ZeroDivisionError, ValueError) as err:
        print("Error",err)

calc()


