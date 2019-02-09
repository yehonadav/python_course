easy = '''\"The ___1___ was worshipped as a goddess in Ancient Egypt,
it was tamed to defend cities against mice;
because of their independent personality,
people nowadays still like them as pets.
For people who prefer a close companion, a ___2___ would be an ideal pet for them:
although it requires daily walking, it will wiggle its tail
when you come home and bark at others.
People who live in cities often have rodents as pets, as they require less space.
The ___3___ is a popular choice
due to its cute small appearance and storing a huge amount of food in its cheek.
Pleasant for you Living space is also a tank full of ___4___,
as they require little effort and are beautiful to watch.\"''' '\n'

easy_solution = ["cat", "dog", "hamster", "fish"]

medium = '''\"___1___ is a fictional character that looks like a pink ball
and can absorb its enemies.
However, ___2___ is the most famous character of Nintendo,
always trying to save Princess Peach.
With its new mobile phone app, ___3___ became popular again,
Gotta catch 'Em all!
Throughout the franchise, Link is trying to rescue Princess ___4___
who is part of the Hyrule's royal family and the titular character.\" ''' '\n'

medium_solution = ["kirby", "super mario", "pokemon", "zelda"]

hard = '''\"Deoxyribonucleic acid (DNA) is a molecule that carries the genetic instructions
in all known living organisms and many viruses.
Each nucleotide is composed of one of
four nitrogen-containing nucleobases - ___1___ (C), ___2___ (G), ___3___ (A) or ___4___ (T),
a sugar called deoxyribose and a phosphate group. \" ''' '\n'

hard_solution = ["cytosine", "guanine", "adenine", "thymine"]


# 1. Start function, set missing_word to 1 and show sample string
# 2. Ask for input of user
# 3. Check if input correlates with arraySolution; if not, turn count goes down.
# User either solves Quiz or Quiz will exit after 5 turns
def find_solution(array_solution, sample, rounds_left):
    missing_word = 1
    print(sample)
    while missing_word <= len(array_solution):
        user = input("What is the word for __" + str(missing_word) + "__ ? ").lower()
        if user != array_solution[missing_word - 1]:
            rounds_left -= 1
            if rounds_left >= 0:
                print("Try again! Only " + str(rounds_left) + " rounds left! " '\n')
            else:
                print("You loose!")
                quit()
        elif user == array_solution[missing_word - 1] and rounds_left > 0:
            print("Correct!" '\n')
            location = "___" + str(missing_word) + "___"
            sample = sample.replace(location, user)
            missing_word += 1
            print(sample)


# Start quiz and ask user which difficulty. Then execute find_solution with user difficulty choice
def start():
    """Ask user for difficulty"""
    user_response = input('''Welcome to your Word replacement Quiz. Please choose your difficulty by entering
'easy' for an animal quiz, 'medium' for Nintendo Geeks or 'hard' for Biologists. ''''\n')
    if user_response.lower() == "easy":
        find_solution(easy_solution, easy, 5)
    elif user_response == "medium":
        find_solution(medium_solution, medium, 3)
    elif user_response == "hard":
        find_solution(hard_solution, hard, 1)
    else:
        print("Please check your input for typo! It should be either easy, medium or hard." '\n')
        start()


if __name__ == "__main__":
    start()
