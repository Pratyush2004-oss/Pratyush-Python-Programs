
# Define your lists
keys = ['name', 'age', 'city']
values = ['Saurav', 19, 'Pithoragarh']

# Initialize an empty dictionary
my_dict = {}

# Ensure both lists are of the same length
if len(keys) == len(values):
    # Combine the lists into a dictionary
    for i in range(len(keys)):
        key = keys[i]
        value = values[i]
        my_dict[key] = value
else:
    print("The lists have different lengths and cannot be combined into a dictionary.")

# Print the resulting dictionary
print(my_dict)


