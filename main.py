from stats import get_num_words, get_num_chars, sort_by_char_count

FILEPATH = "books/frankenstein.txt"

def main():
    text = get_book_text()
    if not text:
        exit(1)
        
    num_words = get_num_words(text)
    num_chars = get_num_chars(text)

    sorted_chars = sort_by_char_count(num_chars)
    print_report(num_words, sorted_chars)

def get_book_text():
    try:
        f = open(FILEPATH)
    except FileNotFoundError:
        print("no file was found in path", FILEPATH)
        return None
    else:
        with f:
            return f.read()


def print_report(word_count, char_counts):
    report = f"""
============ BOOKBOT ============
Analyzing book found at {FILEPATH}...
----------- Word Count ----------
Found {word_count} total words
--------- Character Count -------"""
    
    print(report)
    for entry in char_counts:
        if entry["char"].isalpha():
            print(f"{entry["char"]}: {entry["num"]}")
    
    print("============= END ===============")

if __name__ == "__main__":
    main()