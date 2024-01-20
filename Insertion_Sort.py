# Python code for insertion sort
array = [16, 19, 11, 15, 10, 12, 14]
#iterating over a
for i in array:
    j = array.index(i)
    #i is not the first element
    while j>0:
        #not in order
        if array[j-1] > array[j]:
        #swap
            array[j-1],array[j] = array[j],array[j-1]
        else:
        #in order
            break
        j = j-1

print ("Sorted array is : ",array)

# Sorted array is : [10, 11, 12, 14, 15, 16, 19]



# # Insertion sort in Python
# def insertionSort(array):
#   for step in range(1, len(array)):
#         key = array[step]
#         j = step - 1
#     # Compare key with each element on the left of it until an element smaller than it is found
#     # For descending order, change key<array[j] to key>array[j]. 
#         while j >= 0 and key < array[j]:
#             array[j + 1] = array[j]
#             j = j - 1
#     # Place key at after the element just smaller than it.
#         array[j + 1] = key
