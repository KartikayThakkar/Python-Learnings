for i in range(6):
    print('*' * i)

print("------------------------------")

for i in reversed(range(6)):
    print('*' * i)

print("------------------------------")

for i in range(6):
    print(' ' * (6-i) + '*' * (2*i + 1))

print("------------------------------")

for i in range(1,7):
    print(' ' * (7-i) + '* ' * (i))
