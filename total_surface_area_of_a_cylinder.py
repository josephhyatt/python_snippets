from math import pi

height = float(input("Height of cylinder: "))
radius = float(input("Radius of cylinder: "))

circles = 2 * (pi * radius ** 2)
side = 2 * pi * radius * height
area = circles + side

print("Total surface area = ", round(area, 2))