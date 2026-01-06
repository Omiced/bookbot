def get_num_words(book):
    return len(book.split())

def get_chars_dict(book):
    characters = {}
    for char in book:
        char_lower = char.lower()
        if not char_lower.isalpha():
            continue;
        if char_lower not in characters:
            characters[char_lower] = 1;
        else:
            characters[char_lower] += 1;
    return characters

def sort_on(items):
    return items["num"]

def dict_to_list(dict):
    list = []
    for k,v in dict.items():
        list.append({"char":k,"num":v})
    return list

def sorted_list(list):
    list.sort(reverse=True,key=sort_on)
    return list
    
    
    