import pyglet
from exercises.level_2.games.love_messanger.message_translator import LoveTranslator
from exercises.level_2.games.love_messanger.screen import LoveScreen


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
    LoveScreen(love_msg=LoveTranslator())
    pyglet.app.run()
