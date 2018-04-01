# Lambda Expressions - Anonymous Functions

# a = lambda x,y : x+y
# print(a(2,4))

temp = [32.4,33.5,31.5,37.6,32.8]

f = list(map(lambda cel : 9/5*cel+32, temp))

print(f)

even = list(filter(lambda x:x%2 == 0, [i for i in range(101)]))

print(even)
