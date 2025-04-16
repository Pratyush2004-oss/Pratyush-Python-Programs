a,b,c,i = 1,2,0,0

n = int(input("Enter the number of terms to print in the series : "))
if n==0:
    print (a)
print(f"First {n} terms of the Fibonacci Series is : ")
print(a, end="\t")
print(b, end="\t")
for i in range (n-2):
    c = a+b
    a = b
    b = c
    print(c, end = "\t")

# Enter the number of terms to print in the series : 10
# First  10  terms of the Fibonacci Series is : 
# 1       2       3       5       8       13      21      34      55      89


