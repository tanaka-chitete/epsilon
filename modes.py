from helpers import get_translations, print_translations, write_translations

# TODO: Convert all inputs here and then pass them to get_translations

language_to_number = {
    "all": 0,
    "arabic": 1,
    "german": 2,
    "english": 3,
    "spanish": 4,
    "french": 5,
    "hebrew": 6,
    "japanese": 7,
    "dutch": 8,
    "polish": 9,
    "portuguese": 10,
    "romanian": 11,
    "russian": 12,
    "turkish": 13
}


def run_in_command_line_mode(source_language, target_language, word_to_translate):
    source_number = language_to_number.get(source_language)
    target_number = language_to_number.get(target_language)

    if source_number is None:
        print(f"Sorry, the program doesn't support {source_language}")
    elif target_number is None:
        print(f"Sorry, the program doesn't support {target_language}")
    else:
        translations = get_translations(source_number, target_number, word_to_translate)

        if not translations:
            print(f"Sorry, unable to find {word_to_translate}")
        else:
            print_translations(translations, word_to_translate)
            write_translations(translations, word_to_translate)


def run_in_interactive_mode():
    print("""Hello, you're welcome to the translator. Translator supports:
          1. Arabic
          2. German
          3. English
          4. Spanish
          5. French
          6. Hebrew
          7. Japanese
          8. Dutch
          9. Polish
          10. Portuguese
          11. Romanian
          12. Russian
          13. Turkish""")

    # TODO: Implement error-checking to ensure input is between 1 and 13 inclusive
    print("Type the number of your language:")
    source_number = int(input())

    # TODO: Implement error-checking to ensure input is between 0 and 13 inclusive
    print("Type the number of language you want to translate to or '0' to translate to all languages:")
    target_number = int(input())

    print("Type the word you want to translate:")
    word_to_translate = input()

    translations = get_translations(source_number, target_number, word_to_translate)

    print_translations(translations, word_to_translate)
    write_translations(translations, word_to_translate)
