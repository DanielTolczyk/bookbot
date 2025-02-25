import sys
from stats import word_count

def read_book(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def character_count(book_text):
    count_dict = {}
    text_set = set()
    lower_case_text = book_text.lower()
    for char in lower_case_text:
        if char not in text_set:
            count_dict[char] = 1
            text_set.add(char)
        elif char in text_set:
            count_dict[char] += 1
    return count_dict

def report(word_count, char_count, file_path):
    print(f"--- Begin report of {file_path} ---")
    print(f"{word_count} words found in the document")
    for char in char_count:
        if char.isalpha():
            print(f"{char}: {char_count[char]} times")
    print("--- End report ---")

def main():
    import sys

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_text = read_book(sys.argv[1])
    word_num = word_count(book_text)        
    char_count = character_count(book_text)
    report(word_num, char_count, sys.argv[1])

main()
