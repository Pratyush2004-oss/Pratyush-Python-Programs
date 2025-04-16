num = 0
i = 2
j = 2
for i in range(2,2000000):
    for j in range(2,i+1):
        if i == j:
            # print(i)
            num += i
        elif i%j == 0:
            break

print(f"Sum of all the prime number below 2 million is : {num}")


# 142913828922


