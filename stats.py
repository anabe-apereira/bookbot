
def word_count(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    words = file_contents.split()
    return len(words)

def character_count(text):
    char_count = {}
    text_lower = text.lower()
    for char in text_lower:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    return char_count

def character_sort(char_count_dic):
    sorted_list = []
    for char, count in char_count_dic.items():
        # Only include alphabetical characters
        if char.isalpha():
            sorted_list.append({"char": char, "num": count})
            
    def sort_on(item):
        return item["num"]
    
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
