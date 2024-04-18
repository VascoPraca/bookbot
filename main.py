def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(text)
    count_words(text)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    count = 0
    for word in text.split():
        count += 1
    print(f"Number of words in book: {count}")
    return count
main()