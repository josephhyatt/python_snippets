print("Insert length of proposed triangle: ")
x = float(input("X = "))
y = float(input("Y = "))
z = float(input("Z = "))

if x + y > z and x + y > z and y + z > x:
  print("The triangle of XYZ exists")
else:
  print("The triangle doesn't exist")