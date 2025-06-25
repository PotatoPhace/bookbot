from stats import word_count
from stats import used_charaters
from stats import sort_characters
import sys  

def get_book_text(file):
    return file.read()

def print_report(words, char_count):
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")
    #print(char_count)
    for k in range(0, len(char_count)):
        print(f"{char_count[k]["char"]}: {char_count[k]["num"]}")
    print("============= END ===============")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book = None
    file = "/Users/orange/workspace/bootdotdev/bookbot/books/frankenstein.txt"
    file = sys.argv[1]
    with open(file) as f:
        book = get_book_text(f)

    wd_cnt = word_count(book)
    chars = used_charaters(book)
    chars = sort_characters(chars)

    print_report(wd_cnt, chars)

main()
