import math

x = float(input("Insert length of x: "))
y = float(input("Insert length of y: "))
z = math.sqrt((pow(x, 2) + pow(y, 2)))

area = (x * y) / 2
perimeter = x + y + z

print("Area of right angled triangle = %.2f" % area)
print("Perimeter of right angled triangle = %.2f" % perimeter)