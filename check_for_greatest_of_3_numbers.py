user_input_0 = int(input("Insert 1st number: "))
user_input_1 = int(input("Insert 2nd number: "))
user_input_2 = int(input("Insert 3rd number: "))

print("The biggest number is: ", end="")
if user_input_1 <= user_input_0 >= user_input_2:
  print(user_input_0)
elif user_input_0 <= user_input_1 >= user_input_2:
  print(user_input_1)
elif user_input_0 <= user_input_2 >= user_input_1:
  print(user_input_2)