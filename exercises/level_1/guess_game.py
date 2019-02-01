import random


def print_results(rounds):
    for i in range(len(rounds)):
        print('round {} stats: {}'.format(i + 1, rounds[i]))


def play():
    rounds = []
    while True:
        rounds.append({
            "answer": random.randint(0, 11),
            "guessed_to_high": 0,
            "guessed_to_low": 0,
            "guessed_right": 0
        })
        while True:
            guess = input("\ntype \"exit\" to quit the game\nGuess the number between 1 and 9:")
            if guess == "exit":
                return print_results(rounds)

            guess = int(guess)
            if guess < rounds[-1]['answer']:
                rounds[-1]['guessed_to_high'] += 1
                print("Guess higher!\n")

            elif guess > rounds[-1]['answer']:
                rounds[-1]['guessed_to_low'] += 1
                print("Guess Lower!\n")

            else:
                rounds[-1]['guessed_right'] += 1
                print("Congrats! you guessed right")
                break


if __name__ == "__main__":
    play()
