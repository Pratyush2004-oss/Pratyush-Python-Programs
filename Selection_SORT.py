def selectionSort(array, size):
    for step in range(size):
        min_index = step
        for i in range(step + 1, size):
        # to sort in descending order, change > to < in this line
        # select the minimum element in each loop
            if array[i] < array[min_index]:
                min_index = i
        # put min at the correct position
        (array[step], array[min_index]) = (array[min_index], array[step])

data = [-2, 75, 40, 51, 19, 34,-28]
size = len(data)
selectionSort(data, size)
print('Sorted Array in Ascending Order:')
print(data)

# Sorted Array in Ascending Order:
# [-28, -2, 19, 34, 40, 51, 75]


