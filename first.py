print("Hello")
a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
print("Sum of the given number is : ",a+b)

if ((a+b)%2==0):
    print("Sum of Given number is even")
else:
    print("Sum of Given number is odd")

i = 1
num = int(input("Enter the value : "))
for i in range(1,num+1):
    print(i, end="  -  ")