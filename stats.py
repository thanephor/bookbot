def get_num_words(text):
    return len(text.split())


def get_num_chars(text):
    chars = {}
    for character in text:
        if character.isalpha():
            character = character.lower()
        if character in chars:
            chars[character] += 1
        else:
            chars[character] = 1

    return chars

def sort_by_char_count(char_counts):
    def sort_on(items):
        return items["num"]
    
    res = []
    for char, count in char_counts.items():
        res.append({"char": char, "num" :count})

    res.sort(reverse=True, key=sort_on)
    return res