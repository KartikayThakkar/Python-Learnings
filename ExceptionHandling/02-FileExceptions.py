def greet():
    try:
        file = open('users.txt')
        name = file.readlines()
        # print("Hello "+name)
        for n in name:
            print("Hello "+name)

    except BaseException as err:
        print("Error Occurred...")
        print(err)
        # greet()

    finally:
        print("Finally executed")
        file.close()

greet()