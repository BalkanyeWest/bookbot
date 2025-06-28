from stats import count_words
from stats import count_chars
from stats import sort_dict
import sys

def get_book_text(filePath):
    with open(filePath) as file:
        file_contents = file.read()
    return file_contents

def print_output(path, length, sorted_dict):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {length} total words")
    print("--------- Character Count -------")
    for letter in sorted_dict:
        if letter["char"].isalpha():
            print(f"{letter["char"]}: {letter["num"]}")
    print("============= END ===============")

def main():
    if (len(sys.argv) < 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    book = get_book_text(path)
    length = count_words(book)
    letters = count_chars(book)
    sorted_dict = sort_dict(letters)

    print_output(path, length, sorted_dict)

main()
