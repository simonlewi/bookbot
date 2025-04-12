# Creates a function to split the words in the text
def count_words(text):
    words = text.split()
    return len(words)

def get_count(dict):
    return dict['count']

def count_characters(text):
    # Creates a dictionary to count all separate characters in the book, and converts them all to lowercase to deal with duplicates
    letters_dict = {}

    for char in text:
        lower_char = char.lower()
        if lower_char.isalpha():
            if lower_char in letters_dict:
                letters_dict[lower_char] += 1
            else:
                letters_dict[lower_char] = 1
    
    # Create sorted list of characters
    sorted_list = []
    for char, count in letters_dict.items():
        char_dict = {'character': char, 'count': count}
        sorted_list.append(char_dict)

    # Sort by count in descending order
    sorted_list.sort(key=get_count, reverse=True)

    return sorted_list
