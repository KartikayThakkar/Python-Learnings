def outer():
    print("This is outer")
    def inner():
        print("This is inner")
        def inner_2():
            print("This is inner_2")

        inner_2()

    inner()

outer()
