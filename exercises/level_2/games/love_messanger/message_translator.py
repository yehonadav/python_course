import os
import json
import sys
from googletrans import LANGUAGES


def get_love_sentence_and_filename(sentence: [str]):
    if sentence is None:
        if len(sys.argv) > 1:
            sentence = sys.argv[1:]
        else:
            sentence = ['❤ I love you Zoya ❤', 'Happy Valentine ❤']

    translation_file = f'{__file__.rsplit(os.sep, 1)[0]}{os.sep}{"_".join(sentence).replace(" ", "_")}.json'
    return sentence, translation_file


def create_file(sentence, translation_file):
    if not os.path.exists(translation_file):
        with open(translation_file, 'w') as f:
            json.dump({
                'sentence': sentence,
                'translations': {LANGUAGES['en']: ' '.join(sentence)}
            }, f, indent=2)


class LoveTranslator(dict):
    def __init__(self, sentence=None):
        self.sentence, self.translation_file = get_love_sentence_and_filename(sentence)
        create_file(self.sentence, self.translation_file)
        self.data, self.translations, self.missing_translations = self.get_parameters_from_translation_file()
        dict.__init__(self, self.translations)
        self.translate_love_message()

    def get_parameters_from_translation_file(self):
        with open(self.translation_file) as f:
            data = json.load(f)

        translations: dict = data['translations']
        missing_translations = [ln for ln, language in LANGUAGES.items() if language not in translations]
        return data, translations, missing_translations

    def translate_love_message(self):
        if len(self.missing_translations) > 0:
            from googletrans import Translator
            translator = Translator()

            for ln in self.missing_translations:
                self.translations[LANGUAGES[ln]] = ' '.join(translate.text for translate in translator.translate(self.sentence, dest=ln, src='en'))

            with open(self.translation_file, 'w') as f:
                json.dump(self.data, f, indent=2)
