def main():
    path_to_file = "./books/frankenstein.txt"

    text = get_book_text(path_to_file)
    word_count = get_number_of_words(text)
    letter_counts = get_letter_count(text)
    sorted_letter_counts = get_sorted_results(letter_counts)
    create_report(word_count, sorted_letter_counts)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_number_of_words(text_string):
    words = text_string.split()
    return len(words)


def sort_on(dict):
    return dict["num"]


def get_sorted_results(letter_dictionary):
    results = []
    for key, value in letter_dictionary.items():
        if key.isalpha():
            results.append({"char": key, "num": letter_dictionary[key]})

    results.sort(reverse=True, key=sort_on)
    return results


def get_letter_count(text_string):
    letter_counts = {}
    lowered_string = text_string.lower().strip()
    for letter in lowered_string:
        if letter in letter_counts:
            letter_counts[letter] += 1
        else:
            letter_counts[letter] = 1

    return letter_counts


def create_report(word_count, sorted_letter_counts):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document")
    for count in sorted_letter_counts:
        print(
            f"The '{count["char"]}'' character was found {
                count["num"]} times"
        )


main()
