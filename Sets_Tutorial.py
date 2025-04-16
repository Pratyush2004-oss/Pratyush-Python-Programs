# defining sets
my_set = {1, 2, 3, 4, 5}
my_set2 = {4, 5, 6, 7, 8}

# union of sets
print(my_set | my_set2)  # Output : {1, 2, 3, 4, 5, 6, 7, 8}

# intersection of sets
print(my_set & my_set2)  # Output : {4, 5}

# difference of sets
print(my_set - my_set2)  # Output : {1, 2, 3}

# symmetric difference of sets
print(my_set ^ my_set2)  # Output : {1, 2, 3, 6, 7, 8}

# subset of sets
print(my_set <= my_set2)  # Output : True
print(my_set.issubset(my_set2))  # Output : True

# superset of sets
print(my_set >= my_set2)  # Output : False
print(my_set.issuperset(my_set2))  # Output : False

# length of set
print(len(my_set))  # Output : 5

# clearing set
my_set.clear()  # Output : set()
print(my_set)

# deleting set
del my_set

# remove element from set
my_set2.remove(4)

# copy set
my_set3 = my_set2.copy()
print(my_set3)

# membership testing
print(4 in my_set2)  # Output : True
print(9 in my_set2)  # Output : False