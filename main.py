import sys

from stats import get_num_words, get_num_chars, sort_by_char_count


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]
    text = get_book_text(filepath)
    if not text:
        print("The provided file was empty")
        sys.exit(1)
        
    num_words = get_num_words(text)
    num_chars = get_num_chars(text)

    sorted_chars = sort_by_char_count(num_chars)
    print_report(filepath, num_words, sorted_chars)


def get_book_text(filepath: str) -> str | None:
    try:
        f = open(filepath)
    except FileNotFoundError:
        print("no file was found in path", filepath)
        return None
    else:
        with f:
            return f.read()


def print_report(filepath: str, word_count: int, char_counts: list[dict]):
    report = f"""
============ BOOKBOT ============
Analyzing book found at {filepath}...
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
