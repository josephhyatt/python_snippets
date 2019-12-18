from random import randint

minimum = int(input("Insert minimum number: "))
maximum = int(input("Insert maximum number: "))

x = [randint(minimum, maximum) for i in range(15)]

print(x)