def main():
    word_count = 0
    words = []
    with open("books/frankenstein.txt") as f: 
        global book
        book = f.read()
        words = book.split()
        #print(words)
    for word in words:
        if word != " ":
            word_count += 1
    print(word_count)
    


main()

