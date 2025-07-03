# bookbot

import sys

from stats import word_count
from stats import dictionary_create
from stats import sorted_dictionary_list

def get_book_text(filepath):

    with open(filepath) as f:

        file_contents = f.read()
        return file_contents

def main():

    if (len(sys.argv) != 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    print("============ BOOKBOT ============")

    fileLocation = sys.argv[1]

    print("Analyzing book found at " + fileLocation + "...")

    print("----------- Word Count ----------")

    text = get_book_text("books/frankenstein.txt")
    count = word_count(text)

    print(f"Found {count} total words")

    print("--------- Character Count -------")

    m = dictionary_create(text)
    l = sorted_dictionary_list(m)
    for item in l:
        if(item[0].isalpha()):
            print(item[0] + ": " + f"{item[1]}")

    print("============= END ===============")

main()
