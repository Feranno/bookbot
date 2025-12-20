def get_num_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    words = text.split()
    count_char = {}
    for word in words:
        for i in word:
            i = i.lower()
            count_char[i] = count_char.get(i, 0) + 1    
    return count_char

def sort_on(items):
    return items["count"]

def count_dictionary(count_dict):
    # convert to list of dictionaries with "char" and "count" key values
    count_char = [{"char": char, "count": count} for char, count in count_dict.items()]
    count_char.sort(reverse=True, key=sort_on)
    return count_char