# Defining dictionary
my_dict = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
print(my_dict)

# Accessing values in dictionary
print("\nAccessing values in dictionary")
print(my_dict["name"])  # Output : John
print(my_dict["age"])   # Output : 30
print(my_dict["city"])  # Output : New York

# Deleting values in dictionary
print("\nDeleting values in dictionary")
del my_dict["name"]  # Output : {'age': 30, 'city': 'New York'}
print(my_dict)

# Updating dictionary
print("\nUpdating dictionary")
my_dict["age"] = 31  # Output : {'name': 'John', 'age': 31, 'city': 'New York'}
print(my_dict) 

# Basic dictionary operations
print("\nBasic dictionary operations")
print("Length of dictionary : ", len(my_dict))  # Output : 3
print("\n Adding Dictionary: ")
print(my_dict | {"country": "USA"})  # Output : {'name': 'John', 'age': 31, 'city': 'New York', 'country': 'USA'}

# ITERATION IN DICTIONARY
for key in my_dict:
    print(f"{key} : {my_dict[key]}")

# Built in dictionary functions
print("\nBuilt in dictionary functions")
print("Keys in dictionary : ", my_dict.keys())  # Output : dict_keys(['name', 'age', 'city'])
print("Values in dictionary : ", my_dict.values())  # Output : dict_values(['John', 31, 'New York'])
print("Items in dictionary : ", my_dict.items())  # Output : dict_items([('name', 'John'), ('age', 31), ('city', 'New York')])

# get keys
print("\nget keys")
print(my_dict.get("name"))  # Output : John
print(my_dict.get("country"))  # Output : None