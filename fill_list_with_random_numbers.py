from random import randint

minimum = int(input("Insert minimum number: "))
maximum = int(input("Insert maximum number: "))

y = int(input("Insert range of random numbers: "))

x = [randint(minimum, maximum) for i in range(y)]

print(x)