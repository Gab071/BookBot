import sys
from stats import get_num_words, get_num_characters, chars_dict_to_sorted_list


def get_book_text(book_path: str) -> str:
    with open(book_path) as f:
        file_contents = f.read()

    return file_contents


def print_report(book_path: str, num_words: int, char_count_list: list[tuple[str, int]]):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char_count in char_count_list:
        if char_count[0].isalpha():
            print(f"{char_count[0]}: {char_count[1]}")

    print("============= END ===============")


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    # Uses second argument as the path to the book file
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    num_words = get_num_words(book_text)

    char_count_dict = get_num_characters(book_text)
    char_count_list = chars_dict_to_sorted_list(char_count_dict)

    print_report(book_path, num_words, char_count_list)


main()
