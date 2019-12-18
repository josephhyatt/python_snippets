from math import pi

radius = float(input("Insert radius of the orbit(million km): "))
velocity = float(input("Insert orbital speed(million km/2): "))

radius = radius * 1000000

year = 2 * pi * radius / velocity
year = year / (60 * 60 * 24)
print(round(year))