#print given 3 numbers in ascending order.

num1=int(input("enter 1st number:"))
num2=int(input("enter 2nd number:"))
num3=int(input("enter 3rd number:"))

num=[num1,num2,num3]
num.sort(reverse=True)
print("descending order:",num)