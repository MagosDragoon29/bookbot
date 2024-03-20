def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    low_text = text.lower()
    word_count = get_word_count(text)
    letter_dic = letter_count(low_text)
    #print(letter_dic)
    #print(f"{word_count} words found in the document")
    print(f"--- Begin report of {book_path} ---")
    print("")
    print(f"{word_count} words found in the document.")
    print("")
    for item in letter_dic:
       letter = item['letter']
       number = item['count']
       print (f"The {letter} character was found {number} times.")
    print("")
    print("--- End report ---")

def get_word_count(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def letter_count(text):
    letter_dic = {}
    ordered_letters = []
    for letter in text:
        if letter.isalpha() == True:
            if letter in letter_dic:
                letter_dic[letter] += 1
            else:
                letter_dic.update({letter : 1})
    for character in letter_dic:
        count = letter_dic[character]
        ordered_letters.append({"letter" : character, "count" : count})
    def sort_on(dict):
        return dict["count"]
    ordered_letters.sort(reverse=True, key = sort_on)
    return(ordered_letters)



main()

