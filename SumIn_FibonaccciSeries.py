a,b,c,i = 1,2,0,0
sum = 0
n = int(input("Enter the maximum value : "))

if a%2 == 0:
    sum += a
if b%2 == 0:
    sum += b

while c <= n:
    c = a+b
    a = b
    b = c
    if c%2 == 0:
        sum += c

print(f"Sum of all the even valued terms of Fibonacci Series under {n} is : {sum}")

# Enter the maximum value : 4000000
# Sum of all the even valued terms of Fibonacci Series under  4000000  is :  4613732


