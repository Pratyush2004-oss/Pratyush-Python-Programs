size = int(input("Enter the size of the fibonacci series : "))
a,b = 1,2
print("**************   Fibonacci Series   ***********")
print(f"{a}\t{b}", end="\t")
for i in range(2,size):
    c = a + b
    a = b
    b = c
    print(c,end="\t")
