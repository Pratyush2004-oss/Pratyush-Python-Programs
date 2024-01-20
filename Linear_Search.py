# Linear Search in Python
def linearSearch(array, n, x):
    # Going through array sequencially
    for i in range(0, n):
        if (array[i] == x):
            return i
    return -1

array = [20, 47, 60, 71, 89]
x = int(input("Enter the number to be searched : "))
n = len(array)
result = linearSearch(array, n, x)
if(result == -1):
    print("Element not found")
else:
    print(f"Element found at index: {result}")


