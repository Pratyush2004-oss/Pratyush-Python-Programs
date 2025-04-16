import string

def count_char_frequency(file_path):
    char_frequency = {}
    with open(file_path, 'r') as file:
        text = file.read()
        for char in text:
            if char in char_frequency:
                char_frequency[char] += 1
            else:
                char_frequency[char] = 1
    return char_frequency

def guess_file_type(char_frequency):
    # Common keywords and symbols in Python and C programs
    python_keywords = ['if', 'else', 'for', 'while', 'def', 'import']
    c_keywords = ['int', 'float', 'if', 'else', 'for', 'while', 'return']
    common_symbols = ['{', '}', '(', ')', '[', ']', '=', ';', '+', '-', '*', '/', '#']

    python_score = sum(char_frequency.get(char, 0) for char in string.ascii_letters + string.digits)
    c_score = sum(char_frequency.get(char, 0) for char in string.ascii_letters + string.digits)

    for keyword in python_keywords:
        python_score += char_frequency.get(keyword, 0)

    for keyword in c_keywords:
        c_score += char_frequency.get(keyword, 0)

    for symbol in common_symbols:
        python_score += char_frequency.get(symbol, 0)
        c_score += char_frequency.get(symbol, 0)

    if python_score > c_score:
        return "Python program"
    elif c_score > python_score:
        return "C program"
    else:
        return "Text file"

file_path = input("Enter the file path : ")  # Replace with the path to your file
char_frequency = count_char_frequency(file_path)
file_type = guess_file_type(char_frequency)
print(f"The given file is likely a {file_type}.")