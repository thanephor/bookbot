from stats import get_num_words


def main():
    text = get_book_text("./books/frankenstein.txt")
    if text:
        num_words = get_num_words(text)
        print(f"Found {num_words} total words")

def get_book_text(filepath):
    try:
        f = open(filepath)
    except FileNotFoundError:
        print("no file was found in path", filepath)
        return None
    else:
        with f:
            return f.read()


if __name__ == "__main__":
    main()