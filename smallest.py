#print the least/small number in given two numbers.

num1=int(input("enter first number:"))
num2=int(input("enter second number:"))

if num1 < num2:
    print("num1")
elif(num2 < num1):
    print("num2")
else:
    print("both are equal")