import datetime

while True:
    userMsg = input("Enter your message : ")
    if userMsg == "Hi" or userMsg == "hi":
        print("Hi")
    elif userMsg == "Hello" or userMsg == "hello":
        print("Hello")
    elif userMsg == "Bye" or userMsg == "bye":
        print("Bye")
    elif userMsg == "time":
        time = datetime.datetime.now()
        print("Current time",time.time())
    else:
        print("I don't understand")
