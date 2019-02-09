# ASCII menu spaceships from: http://textart.io/art/tag/spaceship/1
# selection menu from http://www.ascii-code.com/ascii-art/space/planets.php
# planet names generated on http://fantasynamegenerators.com/planet_names.php

import sys
import os
import random
from exercises.level_3.space_game import game_running


def clear_screen():
    # clears the screen
    os.system('cls' if os.name == 'nt' else 'clear')


def open_text(file_path):
    # opens specified text
    temp = open(file_path, 'r')
    print(temp.read())
    temp.close()


def draw_toolbar(name, faction, attack, defence, realm, realm_diff, all_items):
    # draws the toolbar to the screen
    clear_screen()
    print("\nCURRENT SYSTEM: ", realm, "- DIFFICULTY: ", realm_diff, "- PLAYER NAME: ", name, "- FACTION: ", faction,
          "- ATTACK/DEFENCE: ", attack, "/", defence)
    print("CURRENT RESOURCES:", all_items, "\n")


def generate_realm(strength):
    # generates the realm.
    new_place = random.choice(list(open('text/random/places.txt'))).strip()
    market_strength = random.randint(10, 25) / 10
    return new_place, strength, market_strength


def run_battle(ship_data):
    enemy_data = [0, 0]
    # first calculate enemy attack
    enemy_data[0] = (ship_data[1] / 4)
    # then the defence
    enemy_data[1] = (ship_data[0] * 2.5)

    ship_alive = True
    while ship_alive:
        take_damage = True
        print("Captain this enemy ship looks powerful, it could damage us with ", enemy_data[0],
              " in attack, and challenge our weapons by ", enemy_data[1], " in defence.")
        ship_attack_input = input("Your call captain, should we 'attack' or 'repair'?")
        if ship_attack_input == "attack":
            input("The weapons are preparing, lets hope this works...")
            print("FIRE!!!")
            enemy_dodge_chance = random.randint(1, 6)
            if enemy_dodge_chance == 1:
                input("Captain! Our weapons have missed \a")
            elif enemy_dodge_chance == 2:
                print("We have hit the target, damage confirmed. \a")
                enemy_data[1] = enemy_data[1] - (ship_data[0] / 2)
                print("Damage confirmed to be -", ship_data[0] / 2, " enemy defences now at", enemy_data[1])
            else:
                print("We have hit the target, damage confirmed.")
                enemy_data[1] = enemy_data[1] - ship_data[0]
                print("Damage confirmed to be -", ship_data[0], " enemy defences now at", enemy_data[1])

            if enemy_data[1] <= 0:
                input("Captain we have successfully defeated the enemy ship, we can continue with our warp. \a")
                return True, ship_data
        elif ship_attack_input == "repair":
            input(
                "We are sending out specialists to repair the ship right now captain, hopefully this stablize our "
                "defences this turn.")
            repair_chance = random.randint(1, 4)
            if repair_chance == 1:
                input("Captain, the repairs have failed, no support this turn. \a")
            else:
                print("The specialists have been sent out, Captain. \a")
                input("Success! The ship wont take damage this turn.")
                take_damage = False
        input("Captain, the enemy ship is preparing an attack!")
        enemy_no_hit = random.randint(1, 5)
        if enemy_no_hit == 1 or take_damage is False:
            input("We have successfully dodged the enemies attack captain! \a")
        else:
            print("HIT! HIT! Captain, we have been hit. \a")
            ship_data[1] = ship_data[1] - enemy_data[0]
            print("Damage confirmed, we have suffered -", enemy_data[0], "of damage on our ship!")
            if ship_data[1] <= 0:
                input("MAYDAY MAYDAY...")
                input("Your ship has been destroyed, GAME OVER. \a\a\a")
                return False, ship_data
        print("Our ship now stands at ", ship_data[0], " in attack and ", ship_data[1], " in defence, Captain.")
        print("\n-----------------------------------------------------\n")


def play():
    while game_running:
        # show basic menu
        open_text('text/MenuText.txt')
        user_choice = str(input("■ Choose a Option » "))
        clear_screen()

        if user_choice == "start":
            # main game loop
            user_data = [str(input("■ Your Name » ")), str(input("■ Your Faction Name » "))]
            user_resources = [["Gold", 100], ["Tech", 4], ["Fuel", 5], ["Oxygen", 10], ["Water", 10]]
            user_ship_data = [2, 5]  # Attack, Defense
            base_sale_price = [0, 10, 15, 3, 5]
            currently_mined = 0
            setup_complete = True

            current_realm = generate_realm((user_ship_data[0] + user_ship_data[1]) / 2)
            while setup_complete:
                # main part of the game

                draw_toolbar(
                    user_data[0],
                    user_data[1],
                    user_ship_data[0],
                    user_ship_data[1],
                    current_realm[0],
                    current_realm[1],
                    user_resources)
                open_text("text/selectionText.txt")
                selection_user_choice = str(input("■ Choose a Option » "))

                if selection_user_choice == "trade":
                    user_market_choice = input("Welcome to the market, would you like to 'sell' or 'buy': » ")
                    # BUY WOULD TAKE USER TO BUY ATTACK OR DEFENCE ATTRIBUTES,
                    # AT A INCREMENTING COSTS!!! USES 1 TECH EACH TIME.
                    if user_market_choice == "sell":
                        user_sale_choice = int(input(
                            "Which would you like to sell, enter the following\n1 - Tech, 2 - Fuel, 3 - Oxygen, "
                            "4 - Water\n » "))
                        print("Attempting to sell ", user_resources[user_sale_choice][0], " you currently have ",
                              user_resources[user_sale_choice][1])

                        user_sale_amount = int(input("How much would you like to sell? » "))
                        print("Selling ", user_sale_amount, " of ",
                              user_resources[user_sale_choice][0], " would sell for ",
                              base_sale_price[user_sale_choice] * user_sale_amount * current_realm[2])

                        yn_sale = input("y to sell, n to cancel. » ")
                        if yn_sale == "y":
                            if user_sale_amount <= user_resources[user_sale_choice][1]:
                                user_resources[0][1] = user_resources[0][1] + (
                                        base_sale_price[user_sale_choice] * user_sale_amount * current_realm[2])
                                user_resources[user_sale_choice][1] = user_resources[user_sale_choice][1] - user_sale_amount
                            else:
                                input("Not enough resources. » ")

                    elif user_market_choice == "buy":
                        user_upgrade_choice = input(
                            "Each upgrade costs 100 gold and 2 Tech, "
                            "would you like to upgrade 'attack' or 'defence'? » ")
                        if user_resources[0][1] >= 100 and user_resources[2][1] >= 2:
                            user_resources[0][1] = user_resources[0][1] - 100
                            user_resources[1][1] = user_resources[1][1] - 2
                            if user_upgrade_choice == "attack":
                                user_ship_data[0] = user_ship_data[0] + 1
                                input("Ship attack improved by +1 » ")
                            elif user_upgrade_choice == "defence":
                                user_ship_data[1] = user_ship_data[1] + 1
                                input("Ship Defence improved by +1 » ")
                        else:
                            input("Not enough funds... » ")

                elif selection_user_choice == "local":
                    input("You search for one of the missing pages on this new planet, what will you find...")
                    # Pages generated from: http://www.ookii.org/egs/uryuom
                    pages = {
                        'Beginning': 'Obolichot yuc folo, obolichot yuc uvro. Yug\'c gyuno geh votyum cho cgeli...',
                        'New Fortunes': 'Obolichot yum ckuso yuc louji, louji hel ac geh gupo ebol. Mechot quyura cgek ac.',
                        'Journey': 'Ckuso hryutfg yuc u cpyura, vag urceh u seumso. U seumso geh cgok yumgeh cho ampmequm.',
                        'War of the Worlds': 'Obolichot yuc quul, meh nuggol quoug choi gora iea. Quul yuc oboliquoolo.',
                        'Time Will Tell': 'Gyuno yuc cho emri chot quo sumg seumto, iog umiquui.',
                        'End of an Era': 'Cholo yuc u gyuno hel obolichot, umja obolichot yum chyuc quelrja senoc geh um omja. Vag choi quyura urquuic vo u moqu votyummot.',
                        'Power': 'Kequol. Sellakgc. Obolichot.',
                        'Secrets of Space': 'Yum ckuso obolichot yuc fyujjom, quo chyump quo ulo cnulg cholo yuc cenochot 10z cnulgol leamja cho selmol.',
                        'Unknown': 'Chyuc quelrja yuc hara eh ampmequmc. Rogc hyumja chon.'}
                    discovered_page = random.choice(list(pages.items()))

                    print("This note isn't in our language, but reads:\n'" + str(discovered_page[1]),
                          "'\nWhich our computers believe resemble something about The", discovered_page[0], ". ")
                    input(
                        "We will store this is the file Captain, could come in useful later. "
                        "(File will be stored in userData folder)")

                    with open("userData/" + user_data[0] + ".cos",
                              "a+") as storageText:  # dynamically creates folder based on game name.
                        storageText.write(
                            "You discovered The " + str(discovered_page[0]) + " on " + current_realm[
                                0] + ". It read: \n'" +
                            discovered_page[1] + "'\n\n")

                elif selection_user_choice == "mine":
                    if currently_mined <= 4:
                        input("You are about to mine, press ENTER to confirm. » ")
                        currently_mined = currently_mined + 1

                        for resource in user_resources:
                            random_resource_plus = random.randrange(7)
                            print(resource[0], " from ", resource[1], " to ", resource[1] + random_resource_plus)
                            resource[1] = resource[1] + random_resource_plus
                            input("Resource has been added to inventory. ENTER » ")
                    else:
                        input("Already mined this sector » ")

                elif selection_user_choice == "warp":
                    # resets the data
                    current_realm = generate_realm((user_ship_data[0] + user_ship_data[1]) / 2)
                    # get rid of some fuel
                    user_resources[2][1] = user_resources[2][1] - 1
                    user_resources[3][1] = user_resources[3][1] - 1
                    user_resources[4][1] = user_resources[4][1] - 1
                    currently_mined = 0
                    input(
                        "Warping to " + current_realm[0] + ", using 1 of Fuel, Oxygen and Water. ENTER to continue. » ")

                    if user_resources[2][1] == -1 or user_resources[3][1] == -1 or user_resources[4][1] == -1:
                        input("Oh no you attempted to warp and ran out of resources, you loose. ENTER to restart. » ")
                        clear_screen()
                        break

                    enemy_ship_chance = random.randint(1, 4)
                    if enemy_ship_chance == 1 or enemy_ship_chance == 2 or enemy_ship_chance == 3:
                        print("An enemy ship is approaching...")
                        user_escape_choice = input("Would you like to attempt to escape? y or n » ")
                        if user_escape_choice == "y":
                            escape_chance = random.randint(1, 3)
                            if escape_chance == 1:
                                input("You have escaped... » ")
                            else:
                                draw_toolbar(user_data[0], user_data[1], user_ship_data[0], user_ship_data[1],
                                             current_realm[0],
                                             current_realm[1], user_resources)
                                run_battle(user_ship_data)
                        elif user_escape_choice == "n":
                            draw_toolbar(user_data[0], user_data[1], user_ship_data[0], user_ship_data[1],
                                         current_realm[0],
                                         current_realm[1], user_resources)
                            ship_alive, ship_data = run_battle(user_ship_data)
                            if ship_alive is False:
                                clear_screen()
                                break

                # otherwise just reset
                clear_screen()

        elif user_choice == "end":
            sys.exit()
            # quit

        else:
            clear_screen()
            print("unknown input try again")
            # expect new input
