from getpass import getpass
import string


def prepare_to_parse(word):
    """remove all inconsistent letters from input text for parsing."""
    # remove spaces
    word = word.replace(" ", "")
    # changes all letters to lowercase
    word = word.lower()
    for c in word:
        if c in string.punctuation:
            # remove punctuation
            word = word.replace(c, "")
    return word


choices = ["rock", "paper", "scissors"]


def play():
    """this game only works if you run
    the program directly from the terminal"""
    while True:
        player1 = None
        player2 = None

        while player1 not in choices:
            player1 = getpass("PLAYER ONE" + "\n" + "Rock, Paper, or Scissors? Choose! ")
            player1 = prepare_to_parse(player1)
            print("\n")

        while player2 not in choices:
            player2 = getpass("PLAYER TWO" + "\n" + "Rock, Paper, or Scissors? Choose! ")
            player2 = prepare_to_parse(player2)
            print("\n")

        # This is the part that decides who wins.
        if player1 == "rock":
            if player2 == "rock":
                print("It's a TIE! You're both losers.")
            elif player2 == "paper":
                print("Paper hugs rock! Player Two wins!")
            elif player2 == "scissors":
                print("Rock smashes Scissors! Player One wins!")

        elif player1 == "paper":
            if player2 == "rock":
                print("Paper hugs rock! Player One wins!")
            elif player2 == "paper":
                print("It's a TIE! You're both losers.")
            elif player2 == "scissors":
                print("Scissors cut Paper! Player Two wins!")

        elif player1 == "scissors":
            if player2 == "rock":
                print("Rock smashes Scissors! Player Two wins!")
            elif player2 == "paper":
                print("Scissors cut Paper! Player One wins!")
            elif player2 == "scissors":
                print("It's a TIE! You're both losers.")

        if input("Do you want to play another round? (y/n)") == "n":
            break


if __name__ == "__main__":
    play()
