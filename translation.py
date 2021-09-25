class Translation:
    def __init__(self,
                 source_language,
                 target_language,
                 translated_words,
                 source_language_example_sentences,
                 target_language_example_sentences):
        self.source_language = source_language
        self.target_language = target_language
        self.translated_words = translated_words
        self.source_language_example_sentences = source_language_example_sentences
        self.target_language_example_sentences = target_language_example_sentences
