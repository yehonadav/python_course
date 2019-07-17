import random


data = {'choice': str(random.randint(1, 10))}


def set_choice():
    data['choice'] = str(random.randint(1, 10))
    return data['choice']


def get_choice():
    return data['choice']


def play(choice=None):
    print("\n\n\n\n\n\n\n\n\n\n\n")
    print("I chose a number between 1-10")
    print("You have 3 tries to guess my choice.\n")
    if choice is None:
        choice = set_choice()

    for i in range(3):
        guess = input("guess my choice:\n")
        if guess == choice:
            set_choice()
            print("your guess is correct")
            print('you win!')
            return
        else:
            print('poor choice, try again..\n')


def replay():
    play(get_choice())


if __name__ == "__main__":
    print('@---------------- Welcome to my Guess Game ----------------@')
    while True:
        print("\n\n")
        print("Select Menu")
        option = input("""
# (1) new game
# (2) try again
# (3) quit
""")
        if option == '1':
            play()
        elif option == '2':
            replay()
        elif option == '3':
            print('good by')
            break
        else:
            print(f'invalid option {option}, please select 1,2 or 3')
