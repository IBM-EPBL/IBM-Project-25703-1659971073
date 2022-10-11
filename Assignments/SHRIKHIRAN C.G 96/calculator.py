def add(a, b):
   return a + b

def subtract(a, b):
   return a - b

def multiply(a, b):
   return a * b

def divide(a, b):
   return a / b

print("Choose any operation given below:\n")
print("a. Add\nb. Subtract\nc. Multiply\nd. Divide\n")
choice = str(input("Choice: "))
if choice == 'a' or choice == "Add":
   x, y = map(int, input("Enter values: ").split())
   print(x, " + ", y, " = ", add(x, y))

elif choice == 'b' or choice == "Subtract":
   x, y = map(int, input("Enter values: ").split())
   print(x, " - ", y, " = ", subtract(x, y))

elif choice == 'c' or choice == "Multiply":
   x, y = map(int, input("Enter values: ").split())
   print(x, " * ", y, " = ", multiply(x, y))

elif choice == 'd' or choice == "Divide":
   x, y = map(int, input("Enter values: ").split())
   print(x, " / ", y, " = ", divide(x, y))
else:
   print("This is an invalid input")