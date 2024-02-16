print("Select an operation to perform")
print("1. ADD")
print("2. SUBTRACT")
print("3. MULTIPLY")
print("4. DIVIDE")

operation = input()

if operation == "1":
    num = input("Enter first number:")
    num2 = input("Enter second: ")
    print(f"The sum is: {int(num)+ int(num2)}")
elif operation == "2":
    num = input("Enter first number:")
    num2 = input("Enter second number:")
    print(f"The subtraction is: {int(num)-int(num2)}")

elif operation == "3":

    num = input("Enter first number:")
    num2 = input("Enter  second number: ")
    print(f"The multiplication is: {int(num) * int(num2)}")
elif operation == "4":
    num = input("Enter first number:")
    num2 = input("Enter second number: ")
    print(f"The division is: {int(num) / int(num2)}")
else:
    print("INVALID ENTRY")
