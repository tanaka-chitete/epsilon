import sys

def print_translations(translations):
    for t in translations:
        print(f"{t.target_language} Translation:")
        print(t.translated_words[0])

        print()  # Formatting purposes

        print(f"{t.target_language} Example:")
        if t.source_language_sentences and t.target_language_sentences:
            print(f"{t.source_language_sentences[0]}")
            print(f"{t.target_language_sentences[0]}\n")


def write_translations(translations, word_to_translate):
    original_stdout = sys.stdout  # Save reference of the original standard output
    sys.stdout = open(f"{word_to_translate}.txt", "w")  # Redirect output to file

    print("Epsilon (v2.2)")
    print()  # Formatting purposes

    for t in translations:
        print(f"{t.target_language} Translations:")
        for i in range(0, min(5, len(t.translated_words))):  # Print at most 5 translated words
            print(t.translated_words[i])

        print()  # Formatting purposes

        print(f"{t.target_language} Examples:")
        for i in range(0, min(5, len(t.target_language_sentences))):  # Print at most 5 example sentence pairs
            print(f"{t.source_language_sentences[i]}")
            print(f"{t.target_language_sentences[i]}")
            if i < min(5, len(t.target_language_sentences)) - 1:
                print()

    sys.stdout.close()  # Close file
    sys.stdout = original_stdout  # Change standard output back to what it originally was
