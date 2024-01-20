num = int(input("Enter the number : "))
fact = 1
n = num
while n != 0:
    fact = fact*n
    n-=1
print(f"The factorial of {num} is : {fact}")