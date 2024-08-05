import string

def main():

   text = get_book_text("books/frankenstein.txt")
   print(text)
   words = str()
   print(len(words))
   print(character_count(text))
   print_report(words)

def str():
    words = get_book_text("books/frankenstein.txt")
    return words

def get_book_text(path):
    with open(path) as f:
        return f.read()

def character_count(str):
    str = str.lower()
    count = {}
    for i in str:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1

    return count



def print_report(words):
    chars = []
    count = character_count(words)
    alpha = list(string.ascii_lowercase)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{len(words.split())} words found in the document")
    
    for i in count:
        if i.isalpha():  # Ensure the character is an alphabet letter
            dict = {i: count[i]}
            chars.append(dict)

    # Sort the chars list based on the values of each dictionary
    sorted_chars = sorted(chars, key=lambda x: list(x.values())[0], reverse=True)

    for char_dict in sorted_chars:
        char = list(char_dict.keys())[0]
        count = list(char_dict.values())[0]     
        print(f"The {char} character was found {count} times.")
    



main()
