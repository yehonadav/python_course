import pyglet
from exercises.level_2.games.love_messanger.message_translator import LoveTranslator
from exercises.level_2.games.love_messanger.screen import LoveScreen
from exercises.level_2.games.love_messanger.speaker import speaker


if __name__ == "__main__":
    print("""
    XOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOX
    O:::::::::::::::::::::::::::::::::::::::::::::::::::::::O
    X:::::::::::::::::::::::::::::::::::::::::::::::::::::::X
    O::::::::::::           :::::::::           ::::::::::::O
    X:::::::::                :::::                :::::::::X
    O:::::::       *********    :    *********       :::::::O
    X:::::      *****     *****   *****     *****      :::::X
    O::::     ****           *******           ****     ::::O
    X:::     ****              ***              ****     :::X
    O:::     ****               *               ****     :::O
    X::::     ****             BE              ****     ::::X
    O:::::     ****           MINE!           ****     :::::O
    X:::::::     ****                       ****     :::::::X
    O:::::::::     ****                   ****     :::::::::O
    X:::::::::::     ****               ****     :::::::::::X
    O::::::::::::::     ****         ****     ::::::::::::::O
    X:::::::::::::::::     ****   ****     :::::::::::::::::X
    O::::::::::::::::::::     *****     ::::::::::::::::::::O
    X:::::::::::::::::::::::    *    :::::::::::::::::::::::X
    O:::::::::::::::::::::::::     :::::::::::::::::::::::::O
    X::::::::::::::::::::::::::: :::::::::::::::::::::::::::X
    O:::::::::::::::::::::::::::::::::::::::::::::::::::::::O
    X:::::::::::::::::::::::::::::::::::::::::::::::::::::::X
    OXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXO""")
    love_msg = LoveTranslator()
    LoveScreen(love_msg)
    speaker(love_msg)
    pyglet.app.run()
