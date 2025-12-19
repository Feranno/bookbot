def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

def num_words(text):
    words = text.split()
    return len(words)

def main():
    text = get_book_text("books/frankenstein.txt")
    # print(text)
    number_of_words = num_words(text)
    print(f"Found {number_of_words} total words")

main()