def word_count(txt):
    return len(txt.split())

def used_charaters(txt):
    chars = {}
    for char in txt:
        c = char.lower()
        if c in chars:
            chars[c] += 1
        else:
            chars[c] = 1
    return chars

def sort_on(items):
    return items["num"]

def sort_characters(chars):
    char_format = []
    for char in chars:
        char_format.append({"char": char, "num": chars[char]})
    char_format.sort(reverse=True, key=sort_on)
    
    return char_format