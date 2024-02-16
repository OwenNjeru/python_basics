print("Select your option")
print("1. ADD")
print("2. SUBTRACT")
print("3. MULTIPLY")
print("4. DIVIDE")

option = input("My option is:")

if option == "1":
    num = input("Enter the first number")
    num2 = input("Enter the second number")
    print(f"Sum is {int(num)+int(num2)}")
elif option == "2":
    num = input("Enter the first number")
    num2 = input("Enter the second number")
    print(f"Subtraction is{int(num) - int(num2)}")
elif option == "3":
    num = input("Enter the first number")
    num2 = input("Enter the second number")
    print(f"Division is{int(num) / int(num2)}")
elif option == "4":
    num = input("Enter the first number")
    num2 = input("Enter the second number")
    print(f"Multiplication is {int(num) * int(num2)}")
elif option == "5":
    num = input("Enter the first number")
    num2 = input("Enter the second number")
    print(f"Exponential is {int(num) ^ int(num2)}")




