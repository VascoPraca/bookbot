def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(f"--- Begin report of {book_path} ---")
    count_words(text)
    count_letters(text)
    print("--- End report ---")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    count = 0
    for word in text.split():
        count += 1
    print(f"{count} words found in the document\n")

def count_letters(text):
    letters = {}
    for letter in text.lower():
        letters[letter] = letters.get(letter,0)+1
    for key, values in letters.items():
        if key in "abcdefghijklmnopqrstuvwxyz":
            print(f"The '{key}' character was found {values} times")

main()