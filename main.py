def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    text_characters = get_characters(text)
    chars_sorted_list = chars_dict_to_sorted_list(text_characters)
    print(f"--- Begin report of {book_path} ---")
    print(f"{get_word_count(text)} words found in the document\n")
    
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")
    


def sort_on(dict):
    return dict["num"]

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for char in num_chars_dict:
        sorted_list.append({"char": char, "num": num_chars_dict[char]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(text):
    return len(text.split())

def get_characters(text):
    character_counts = {}
    for char in text.lower():
        if char in character_counts:
            character_counts[char] = character_counts[char] + 1
        else:
            character_counts.update({char: 1})
    return character_counts      

main()

