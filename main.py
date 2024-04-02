def main():

    book_name = input("Please enter the name of the book or work you want analyzed:").lower()
    book_path = f"books/{book_name}.txt"
    file_contents = find_book(book_path)


    report(word_count(file_contents),letter_count(file_contents))

def find_book(book_path):
    try:
        file_contents = open(f"{book_path}").read()
        return file_contents
    except FileNotFoundError:
        print("That book or work is not in our library, please try another")
        exit()
    

def word_count(file_contents):
    words = file_contents.split()
    return (len(words))


def letter_count(file_contents):
    letters_dict = {}

    for letter in file_contents:
        character = letter.lower()
        if character in letters_dict:
            letters_dict[character] += 1
        else:
            letters_dict[character] = 0

    return letters_dict


def report(word_count,letter_count):

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document")
    for key, value in letter_count.items():
        if key.isalpha():
            print(f"The {key} character was found {value} times")
    print("--- End report ---")
    

main()
