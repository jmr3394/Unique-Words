# Python3
import string
# Define main program
def main():
    # Define variables
    total_word_count = 0
    unique_word_count = 0
    unique_words = ''
    # User enters words file with extension
    input_file = input('Enter file name for word list: ')
    # Open words file
    with open(input_file, 'r') as words_file:
        # Read all words from file
        all_words = words_file.read()
        # Strip punctuation
        all_words_cleaned = all_words.translate(str.maketrans('', '', string.punctuation))
        # Write all words to list
        word_list = all_words_cleaned.split()
        # Loop through word list
        for word in word_list:
            total_word_count = total_word_count + 1
        # Find unique words
        unique_word_list = set(word_list)
        # Loop through unique words list
        for word in unique_word_list:
            unique_word_count = unique_word_count + 1
            unique_words += word + '\n'
    # Print all unique words
    print('Unique Words: ')
    print(unique_words)
    # Write unique words to output file
    with open('unique_words.txt', 'w') as output_file:
        output_file.write(unique_words)
    # Print word counts
    print('Total words: ',total_word_count)
    print('Unique words: ',unique_word_count)

main()
