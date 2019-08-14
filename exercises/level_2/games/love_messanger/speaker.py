import time
import pyttsx3
from threaders import threaders
from exercises.level_2.games.love_messanger.message_translator import LoveTranslator


@threaders.threader()
def speaker(love_msg: LoveTranslator):
    engine = pyttsx3.init()
    while True:
        for ln, translation in love_msg.items():
            translation = translation.replace('❤', '')
            engine.say(ln)
            engine.runAndWait()
            engine.say(translation)
            engine.runAndWait()
            time.sleep(1)
