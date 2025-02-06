
def read_book(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def word_count(book_text):
    words = book_text.split()
    count = len(words)
    return count

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

def report(word_count, char_count):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in this document")
    for char in char_count:
        if char.isalpha():
            print(f"The '{char}' character was found {char_count[char]} times")
    print("--- End report ---")


def main():
    
    book_text = read_book("books/frankenstein.txt")
    word_num = word_count(book_text)        
    char_count = character_count(book_text)
    report(word_num, char_count)

main()