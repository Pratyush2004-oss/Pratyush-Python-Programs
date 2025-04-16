# Defining lists
my_list = [1, 2, "Hello", True, 3.14, [1, 2, 3]]

# accessing values in list
print("\nAccessing values in list")
print(my_list[0])   # Output : 1, zero-based indexing
print(my_list[3])   # Output : True
print(my_list[-1])  # Output : [1, 2, 3], Print list from last

# Deleting values in list
print("\nDeleting values in list")
del my_list[0]      #delete element at index 0
print(my_list)      # Output : [2, "Hello", True, 3.14, [1, 2, 3]]

print("\nDeleting values in list ny passing the value")
my_list.remove(3.14) #remove element 3.14
print(my_list)       # Output : [2, "Hello", True, [1, 2, 3]]

# updating list
print("\nUpdating list")
my_list[1] = "Welcome"
print(my_list)       # Output : [2, "Welcome", True, [1, 2, 3]]

# Basic list operations
print("\nBasic list operations")
print("Length of list : ", len(my_list))    # Output : 4
print("\n Adding List: ")
print(my_list + [4, 5, 6])  # Output : [2, "Welcome", True, [1, 2, 3], 4, 5, 6]
print("\n Repetation of List: ")
print(my_list * 3)   # Output : [2, "Welcome", True, [1, 2, 3], 2, "Welcome", True, [1, 2, 3], 2, "Welcome", True, [1, 2, 3]]
print("Membership : ")
print(3 in my_list)     # Output : False
print(2 in my_list)     # Output : True

# Built in functions in list
print("\nBuilt in functions in list")
my_list2 = [10,75,87,96,45,25,85]
print("Maximum element in list 2 is ", max(my_list2))  # Output : 96
print("Minimum element in list 2 is ", min(my_list2))  # Output : 10
print("Sum of all elements in list 2 is " ,sum(my_list2))  # Output : 423
print("List in sorted order : ", sorted(my_list2)) 
 
my_list2.reverse()  # reverse the list
print("List in reversed order : ",my_list2)
