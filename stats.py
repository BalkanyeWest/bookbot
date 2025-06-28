def count_words(text):
    words = text.split()
    return len(words)

def count_chars(text):
    count = {}
    for letter in text:
        if letter.lower() not in count:
            count[letter.lower()] = 0
        count[letter.lower()] += 1
    return count

def sort_on(items):
    return items["num"]

def sort_dict(dict):
    list = []
    for key, value in dict.items():
        list.append({"char": key, "num": value})
    list.sort(reverse=True, key=sort_on)
    return list
