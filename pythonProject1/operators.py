 # arithmetic operators, assignment, logical, comparison

num = 43 #first operand
num2 = 12 #second operand

#Arithmetic operand
print(f"the sum of {num} and {num2} is {num+num2}")
print(f"the difference of {num} and {num2} is {num-num2}")
print(f"the division of {num} and {num2} is {num/num2}")
print(f"the multiplication of {num} and {num2} is {num*num2}")
print(f"the remainder of {num} and {num2} is {num%num2}")
print(f"the exponent of {num} and {num2} is {num**num2}")
print(f"the flow of {num} and {num2} is {num//num2}")

num3 = 56
num4 = 23

#Comparison operators

print(f"{num3} and {num4} are equal {num3 == num4}")
print(f"{num3} and {num4} are not equal {num3 != num4}")
print(f"{num3} is greater than or equal to {num4} {num3 >= num4}")
print(f"{num3} is lesser than or equal to {num4} {num3 <= num4}")

# Assignment operators

num5 = 27
num6 = 8

print(f"num5 = num6:{num5==num6} ")
print(f"num5 += num6:{num5+num6} ")
print(f"num5 *= num6:{num5*num6} ")
print(f"num5 /= num6:{num5/num6} ")

# logical operator

num7 = 10
print(f"one statement is {num7>=15 or num7<12}")
print(f"one statement is {num7>=15 and num7<12}")
