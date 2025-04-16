def count_unique_words(filename):
    unique_words = set()
    with open(filename, 'r') as file:
        for line in file:
            words = line.split()
            unique_words.update(words)  # Add words to the set

    return len(unique_words)

filename = 'Dummy.txt'  # Replace with your actual file name
unique_word_count = count_unique_words(filename)
print(f"Unique words in '{filename}': {unique_word_count}")
