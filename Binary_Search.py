# Binary Search in python
def binarySearch(array, x, low, high):
  # Repeat until the pointers low and high meet each other
    while low <= high:
        mid = low + (high - low)//2
        if array[mid] == x:
            return mid
        elif array[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1

array = [33, 44, 15, 26, 67, 28, 79, 8]
# Sorting array in ascending order
array.sort()
print("Array is : ",array)

x = int(input("Enter the number to be Searched : "))
result = binarySearch(array, x, 0, len(array)-1)
if result != -1:
    print(f"Element is present at index {str(result)}")
else:
    print("Not found")


