from translator import get_translations
from user_interface import input_int, input_string
from output import print_translations, write_translations
from textwrap import dedent

TRANSLATE = 1

def main():
    print()  # For formatting purposes
    while True:
        main_menu = """\
            Epsilon (v.2.3)
            
            1. Translate
            0. Quit
            """
        print(dedent(main_menu))
        user_input = input_int(0, 1, "Operation: ")
        print()  # For formatting purposes

        if user_input == TRANSLATE:
            translate()
        else:
            break


def translate():
    source_languages_menu = """\
        Source Language

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
        13. Turkish
        """
    print(dedent(source_languages_menu))
    source_number = input_int(1, 13, "Language: ")

    print()  # For formatting purposes

    target_languages_menu = """\
        Target Language

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
        13. Turkish
        """
    print(dedent(target_languages_menu))
    target_number = input_int(0, 13, "Language: ")

    print()  # For formatting purposes

    word_to_translate = input_string("Word to translate: ")

    if source_number == target_number:
        print("Source and target languages cannot be the same")
    else:
        print("\nTranslating...\n")

        translations = get_translations(source_number, target_number, word_to_translate)
        if translations:
            print_translations(translations)
            write_translations(translations, word_to_translate)


if __name__ == "__main__":
    main()
