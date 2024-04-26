def main():
    #update path for other inputs
    def_path = "books/frankenstein.txt"
    words = load_book_text(def_path)
    num__words = word_counter(words)
    num_letters = letter_counter(words)
    print(f"------ BEGIN REPORT OF {def_path}------")
    print(f"Number of words in this book: {num__words}")
    gen_report(num_letters)
    print(f"------END OF REPORT------")

def load_book_text(path):
    with open(path) as f:
        return f.read()

#function for counting words
def word_counter(in_string):
    counter = 0
    #split by whitespaces
    words = in_string.split()
    for word in words:
        if word:
            counter += 1
    return counter

#function to count letters
def letter_counter(in_string):
    lowered_string = in_string.lower()
    dict_num_letters = {}
    for i in lowered_string:
        if i in dict_num_letters.keys():
            dict_num_letters[i] = dict_num_letters.get(i) + 1
        else:
            dict_num_letters[i] = 1
    return dict_num_letters

#function for sort by number
def sort_on(dict):
    return dict["num"]

#function to sort charachters from max to min
def gen_report(in_dict):
    report_letters = []
    #create list of dicts and sort it
    for item in in_dict.keys():
        if item.isalpha():
            report_letters.append({"char":item, "num":in_dict[item]})
    report_letters.sort(reverse=True, key=sort_on)
    #print it fancy
    for i in range(len(report_letters)):
        print(f"The '{report_letters[i].get("char")}' character was found {report_letters[i].get("num")} times")

main()