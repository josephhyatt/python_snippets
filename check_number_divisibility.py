numerator = int(input("Insert the numerator: "))
denominator = int(input("Insert the denominator: "))
is_divisible = int(denominator / numerator)

if numerator % denominator:
  print("Yes!", numerator, "is divisible by", denominator, ", and the answer is",is_divisible)
else:
  print("No!", numerator, "is not divisible by", denominator)