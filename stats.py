def get_num_words(book_text: str) -> int:
    words = book_text.split()
    num_words = len(words)

    return num_words


def get_num_characters(book_text: str) -> dict[str, int]:
    char_count_dict = dict()
    characters = set()

    for char in book_text:
        if char.lower() not in characters:
            char_count_dict[char.lower()] = 1
            characters.add(char.lower())
        else:
            char_count_dict[char.lower()] += 1

    return char_count_dict


def sort_on(character_count: tuple[str, int]) -> int:
    return character_count[1]


def chars_dict_to_sorted_list(chars_dict: dict[str, int]) -> list[tuple[str, int]]:
    char_count_list = []
    for char in chars_dict:
        char_count_list.append((char, chars_dict[char]))

    char_count_list = sorted(char_count_list, reverse=True, key=sort_on)

    return char_count_list
