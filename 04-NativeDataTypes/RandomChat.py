import random

welcomeMessages = ['Hi', 'Hey', 'Hello', 'Welcome']

byeMessages = ['Bye', 'See you later', 'Bie', 'Visit Again','Ok']

while True:
    userMsg = input("Enter your message : ")
    welcome = random.choice(welcomeMessages)
    bye = random.choice(byeMessages)

    if userMsg.startswith('H') or userMsg.startswith('h'):
        print(welcome)
    elif userMsg.startswith('B') or userMsg.startswith('b'):
        print(bye)
    else:
        print("I don't understand")
