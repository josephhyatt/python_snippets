x = float(input("Insert coordinates of point X: "))
y = float(input("Insert coordinates of point Y: "))

if x > 0 and y > 0:
  print("The first quadrant")
elif x < 0 and y > 0:
  print("The second quatrant")
elif x < 0 and y > 0:
  print("The third quatrant")
elif x < 0 and y < 0:
  print("The second quatrant")
elif x == 0 and y == 0:
  print("Point of origin")
elif x == 0:
  print("X point")
elif y == 0:
  print("Y point")