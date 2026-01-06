from stats import get_num_words, get_chars_dict, sorted_list, dict_to_list
import sys

def get_book_text(file_path):
    with open(file_path, encoding="utf-8-sig") as f:
        return f.read()

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book = get_book_text(sys.argv[1])
    # print(get_book_text("./books/frankenstein.txt"))
    # print(get_chars_dict(book))
    sortedList = sorted_list(dict_to_list(get_chars_dict(book)))
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(book)} total words")
    for dict in sortedList:
        print(f"{dict["char"]}: {dict["num"]}")
main()