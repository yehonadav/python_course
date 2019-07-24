import os
import sys
import time
import json
import datetime
from exercises.level_1.oop.fight_club.resources.menus import start_menu
from exercises.level_1.oop.fight_club.resources.characters import players
from exercises.level_1.oop.fight_club.utils.render import render
from exercises.level_1.oop.fight_club import conf
from traceback import format_exc as error


class Menu:
    def __init__(self, game):
        self.game = game

    def start(self):
        choices = {
            'quit': '0',
            'new game': '1',
            'load game': '2'
        }
        while True:
            time.sleep(1)
            render(start_menu.start_menu)
            choice = input(':')
            try:
                if choice == choices['quit']:
                    self.game.exit()
                elif choice == choices['new game']:
                    self.select_name()
                elif choice == choices['load game']:
                    self.load_game()
                else:
                    print('invalid choice, try again', end='\r')
            except:
                print(error())

    def load_game(self):
        print("not implemented yet")

    def select_name(self):
        choices = {
            'go back': '0',
        }
        while True:
            time.sleep(1)
            render(start_menu.select_name)
            choice = input(':')
            try:
                if choice == choices['go back']:
                    return
                else:
                    date = datetime.datetime
                    name_file = f'{conf.database_dir}\\{choice}_{date.year}_{date.month}_{date.day}_{date.hour}_{date.min}_{date.second}.json'
                    i = 0
                    while os.path.exists(name_file):
                        name_file = f'{name_file}_{i}'
                        i += 1

                    self.game.data['name'] = choice
                    self.game.file = name_file
                    self.game.save()

                    return self.select_characters()
            except:
                print(error())

    def select_characters(self):
        choices = {
            'go back': '0',
        }
        for i, player in enumerate(players):
            choices[player.__class__.__name__] = str(i+1)
        characters = ''.join([f'({i+1}) {player.__class__.__name__}' for i, player in enumerate(players)])

        while True:
            time.sleep(1)
            render(start_menu.select_characters+characters)
            choice = input(':')
            try:
                if choice == choices['go back']:
                    return
                elif choice in choices.values():
                    self.game.data['character'] = choice
                    self.game.save()
                    self.play_manu()
                else:
                    print('invalid choice, try again', end='\r')
            except:
                print(error())

    def play_manu(self):
        choices = {
            'go back': '0',
        }
        while True:
            time.sleep(1)
            render(start_menu.select_characters)
            choice = input(':')
            try:
                if choice == choices['go back']:
                    return
                else:
                    date = datetime.datetime
                    name_file = f'{conf.database_dir}\\{choice}_{date.year}_{date.month}_{date.day}_{date.hour}_{date.min}_{date.second}.json'
                    i = 0
                    while os.path.exists(name_file):
                        name_file = f'{name_file}_{i}'
                        i += 1

                    with open(name_file, 'w') as f:
                        json.dump({'name': choice}, f)

                    return self.select_characters()
            except:
                print(error())
