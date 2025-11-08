import sys
from stats import word_count , character_count, character_sort

def get_book_text(path_to_file):  
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def print_report(book_path,word_count,char_sorted):
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")

    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")

    print("--------- Character Count -------")    

    for char_dict in char_sorted:
        char = char_dict["char"]
        count = char_dict["num"]
        print(f"{char}: {count}")
    
    print("============= END ===============")

def main():
    if len(sys.argv)<= 1:
        print(" Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_path = sys.argv[1]
        book_text = get_book_text(book_path)
        word_counted = word_count(book_path)
        char_sorted = character_sort(character_count(book_text))
        print_report(book_path, word_counted, char_sorted)
main()