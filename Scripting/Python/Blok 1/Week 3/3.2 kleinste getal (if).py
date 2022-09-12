# print the smallest of 3 numbers entered by the user
# get the numbers from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))
# find the smallest number
if num1 < num2 and num1 < num3:
   smallest = num1
elif num2 < num1 and num2 < num3:
   smallest = num2
else:
   smallest = num3
# print the result
print("The smallest number is", smallest)