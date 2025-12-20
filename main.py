from stats import get_num_words
from stats import count_characters
from stats import count_dictionary
import sys

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()
    

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    text = get_book_text(sys.argv[1])
    # print(text)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    number_of_words = get_num_words(text)
    print(f"Found {number_of_words} total words")
    print("--------- Character Count -------")
    count_char = count_characters(text)
    count_dict = count_dictionary(count_char)
    
    #iterate through the list of dictionaries
    for dict in count_dict:
        char = dict['char']
        count = dict['count']
        print(f"{char}: {count}")
    
main()