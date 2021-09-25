from translator import get_translations
from output import print_translations, write_translations
from textwrap import dedent

def main():
    print("\nEpsilon (v2.0)\n")

    source_languages_menu = """\
        Source Languages
        1.  Arabic
        2.  Dutch
        3.  English
        4.  French
        5.  German
        6.  Hebrew
        7.  Japanese
        8.  Polish
        9.  Portuguese
        10. Romanian
        11. Russian
        12. Spanish
        13. Turkish"""
    print(dedent(source_languages_menu))
    print("Source language number: ", end="")
    source_number = int(input())
    # source_number = scan_int("Source language number: ", 1, 13)  # TODO: Implement user_input.py class

    print()  # Formatting purposes

    target_languages_menu = """\
        Target Languages
        0.  All languages
        1.  Arabic
        2.  Dutch
        3.  English
        4.  French
        5.  German
        6.  Hebrew
        7.  Japanese
        8.  Polish
        9.  Portuguese
        10. Romanian
        11. Russian
        12. Spanish
        13. Turkish"""
    print(dedent(target_languages_menu))
    print("Target language number: ", end="")
    target_number = int(input())
    # target_number = scan_int("Target language number: ", 0, 13)  # TODO: Implement user_input.py class

    print()  # Formatting purposes

    print("Word to translate: ", end="")
    word_to_translate = input()
    # word_to_translate = scan_string("Word to translate: ")

    print()  # Formatting purposes

    print("Translating...")

    print()  # Formatting purposes

    if source_number == target_number:
        print("Language numbers cannot denote the same language")
    else:
        translations = get_translations(source_number, target_number, word_to_translate)
        if translations:
            print_translations(translations)
            write_translations(translations, word_to_translate)


if __name__ == "__main__":
    main()
