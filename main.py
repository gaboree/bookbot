def main():
    def_path = "books/frankenstein.txt"
    words = load_book_text(def_path)
    num__words = word_counter(words)
    print(num__words)

def load_book_text(path):
    with open(path) as f:
        return f.read()

def word_counter(in_string):
    counter = 0
    words = in_string.split()
    for word in words:
        if word:
            counter += 1
    return counter

main()