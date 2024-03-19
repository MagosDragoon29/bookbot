def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    low_text = text.lower()
    word_count = get_word_count(text)
    letter_dic = letter_count(low_text)
    print(letter_dic)
    print(f"{word_count} words found in the document")

def get_word_count(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def letter_count(text):
    letter_dic = {
        'a':0 , 'b':0 , 'c':0 , 'd':0 , 'e':0,
        'f':0 , 'g':0 , 'h':0 , 'i':0 , 'j':0,
        'k':0 , 'l':0 , 'm':0 , 'n':0 , 'o':0,
        'p':0 , 'q':0 , 'r':0 , 's':0 , 't':0,
        'u':0 , 'v':0 , 'w':0 , 'x':0 , 'y':0,
        'z':0
        }
    for letter in text:
        if letter in letter_dic:
            letter_dic[letter] += 1
    return(letter_dic)


main()

