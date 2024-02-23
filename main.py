print("--- Begin report of frankenstein.txt ---")

# Creates a function to split the words in the text
def count_words(text):
    words = text.split()
    return len(words)

def get_count(dict):
    return dict['count']

# Opens the text file of the book and prints the amount of words included in the file
def main():
    with open("books/frankenstein.txt") as f:
        file_content = f.read()
        num_words = count_words(file_content)
        print(f"there are {num_words} of words in the book.")
    
    # Creates a dictionary to count all separate characters in the book, and converts them all to lowercase to deal with duplicates
    letters_dict = {}

    for char in file_content:
        lower_char = char.lower()
        if lower_char.isalpha():
            if lower_char in letters_dict:
                letters_dict[lower_char] += 1
            else:
                letters_dict[lower_char] = 1
    
    # Prints out a list in descending order of all the characters that were found in the text 
    sorted_list = []
    for char, count in letters_dict.items():
        char_dict = {'character': char, 'count': count}
        sorted_list.append(char_dict)
        sorted_list.sort(key=get_count, reverse=True)
    
    for entry in sorted_list:
        print(f"The '{entry['character']}' character was found {entry['count']} times")

    print("--- End report ---")


main()

