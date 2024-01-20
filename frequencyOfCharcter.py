
# Define a function that takes a file name and a character as parameters
def count_frequency(file_name, char):
    # Initialize a counter variable to zero
    count = 0
    # Open the file in read mode
    with open(file_name, "r") as file:
        # Loop through each line in the file
        for line in file:
            # Loop through each character in the line
            for c in line:
                # If the character matches the given character, increment the counter
                if c == char:
                    count += 1
    # Return the counter value
    return count

# Ask the user for a file name and a character
file_name = input("Enter the file name: ")
char = input("Enter the character: ")

# Call the function and print the result
result = count_frequency(file_name, char)
print(f"The frequency of {char} in {file_name} is {result}.")


