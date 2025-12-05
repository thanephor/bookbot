
def get_num_words(text: str) -> int:
    return len(text.split())


def get_num_chars(text: str) -> dict:
    chars = {}
    for character in text:
        if character.isalpha():
            character = character.lower()
        if character in chars:
            chars[character] += 1
        else:
            chars[character] = 1

    return chars


def sort_by_char_count(char_counts: dict) -> list[dict]:
    res: list[dict] = []
    for char, count in char_counts.items():
        res.append({"char": char, "num" :count})

    res.sort(reverse=True, key=lambda items: items["num"])
    return res
