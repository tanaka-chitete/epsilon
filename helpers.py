import requests
import sys
from bs4 import BeautifulSoup
from translation import Translation


languages = [
    "arabic",
    "german",
    "english",
    "spanish",
    "french",
    "hebrew",
    "japanese",
    "dutch",
    "polish",
    "portuguese",
    "romanian",
    "russian",
    "turkish"
]


def get_translations(source_number, target_number, word_to_translate):
    source_index = source_number - 1  # Convert to zero-based index
    if target_number == 0:
        start_target_index = 0
        end_target_index = len(languages)
    else:
        start_target_index = target_number - 1  # Convert to zero-based index
        end_target_index = target_number

    translations = list()
    source_language = languages[source_index]
    session = requests.Session()  # Create session to speed up get requests
    for i in range(start_target_index, end_target_index):
        if i != source_index:  # Prevent translating to the same language
            try:
                # Convert short form languages to their long-form equivalents
                target_language = languages[i]

                # Contact API
                url = f"https://context.reverso.net/translation/{source_language.lower()}-{target_language.lower()}/{word_to_translate}"
                headers = {'User-Agent': 'Mozilla/5.0'}
                response = session.get(url, headers=headers)

                response.raise_for_status()  # Raises HTTPError, if one occurs

                # Attempt to parse response
                if response.status_code == 200:
                    translations.append(parse_response(source_language, target_language, response))
            except requests.exceptions.HTTPError:
                print(f"Sorry, unable to find {word_to_translate}")
                break

    return translations


def parse_response(source_language, target_language, response):
    translated_words = list()
    source_language_example_sentences = list()
    target_language_example_sentences = list()

    soup = BeautifulSoup(response.content, "html.parser")

    for a in soup.find_all("a", {"class": ["translation", "ltr", "dict"]}):
        translated_words.append(a.text.strip())
    translated_words = translated_words[1:]  # Remove unnecessary "Translation" string from the beginning of the list

    for div in soup.find_all("div", {"class": "src"}):
        source_language_example_sentences.append(div.text.strip())

    for div in soup.find_all("div", {"class": "trg"}):
        target_language_example_sentences.append(div.text.strip())

    return Translation(source_language,
                       target_language,
                       translated_words,
                       source_language_example_sentences,
                       target_language_example_sentences)


def print_translations(translations, word_to_translate):
    output_translations(translations, word_to_translate)


def write_translations(translations, word_to_translate):
    original_stdout = sys.stdout  # Save reference of the original standard output
    sys.stdout = open(f"{word_to_translate}.txt", "w")  # Redirect output to file
    output_translations(translations, word_to_translate)  # Output translations to file
    sys.stdout.close()  # Close file
    sys.stdout = original_stdout  # Change standard output back to original


def output_translations(translations, word_to_translate):
    for t in translations:
        # print(f"{t.target_language} Translations:")
        # for i in range(0, min(5, len(t.translated_words))):  # Print at most 5 translated words
        #     print(t.translated_words[i])
        print(f"{t.target_language} Translation:")
        print(t.translated_words[0])

        print()  # Format terminal output

        # print(f"{translations.target_language} Examples:")
        # for i in range(0, min(5, len(translations.target_language_example_sentences))):  # Print at most 5 example sentence pairs
        #     print(f"{translations.source_language_example_sentences[i]}\n{translations.target_language_example_sentences[i]}\n")
        print(f"{t.target_language} Example:")
        if t.source_language_example_sentences and t.target_language_example_sentences:
            print(f"{t.source_language_example_sentences[0]}\n{t.target_language_example_sentences[0]}\n")
