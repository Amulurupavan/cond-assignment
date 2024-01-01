#print the greatest number in given three numbers.

num1=int(input("enter first number:"))
num2=int(input("enter second number:"))
num3=int(input("enter third number:"))

if num1 > num2 and num1 > num3:
    print("num1")
elif num3 < num2:
    print("num2")
else:
    print("num3")