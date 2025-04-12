from stats import count_words, count_characters
from sys import argv, exit

# Opens the text file of the book and prints the amount of words included in the file
def main():
    
    print("============ BOOKBOT ============")


    if len(argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        return exit(1)
    else:
        file_path = argv[1]


    print(f"Analyzing book found at {file_path}")
    with open(file_path) as f:
        file_content = f.read()

        print("----------- Word Count ----------")
        # Get word count
        num_words = count_words(file_content)
        print(f"Found {num_words} total words")

        print("--------- Character Count -------")
        # Get character count
        char_counts = count_characters(file_content)

        for entry in char_counts:
            print(f"{entry['character']}: {entry['count']}")

    
    print("============= END ===============")

main()

