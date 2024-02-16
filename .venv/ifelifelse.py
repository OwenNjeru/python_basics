marks = int(input("Enter marks:"))
if marks > 85 and marks <= 100:
    print("Congrats! You scores grade A...")
elif marks > 60 and marks <= 85:
    print("You scores grade B+...")
elif marks > 40 and marks <= 60:
    print("You scores grade B...")
elif marks > 30 and marks <= 40:
    print("You scores grade c...")
else:
    print("Aim higher")
