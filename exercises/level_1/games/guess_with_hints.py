class GuessGame:
    import sys

    if len(sys.argv) > 1:
        guess = sys.argv[1]
    else:
        guess = "piggy love bunny"

    words = guess.split(' ')
    words_length = len(words)
    hint_word_edges_range = range(2 + words_length, 2 + 3 * words_length, 2)

    def __init__(self):
        self.hints = 0
        self.tries = 1

    def guess_is_correct(self):
        if self.tries == 1:
            print("you guessed correctly")
            print("amazinggggg!!")
        else:
            print(f"you guessed correctly after {self.tries} tries")
            if self.hints == 0:
                print("amazing")
            elif self.hints == 1:
                print("awesome")
            elif self.hints == 2:
                print("very good")
            elif self.hints == 3:
                print("nice try")
            elif 3 < self.hints < 7:
                print(f"and it only took you {self.hints} hints")
            else:
                print(f"with {self.hints} hints ..")

    def hint_the_word_size_of_the_sentence(self):
        if self.hints == 1:
            print(f"answer has {self.words_length} words")
            return True

    def hint_the_letter_size_of_a_word(self):
        if 1 < self.hints < self.words_length + 2:
            word_index = self.hints - 2
            word = self.words[word_index]
            print(f"answer's word{word_index + 1} has {len(word)} letters")
            return True

    def hint_the_edges_of_a_word(self):
        if self.words_length + 1 < self.hints < 2 + 3 * self.words_length:
            word_index = 0
            for i, hint in enumerate(self.hint_word_edges_range):
                if self.hints in (hint, hint + 1):
                    word_index = i
                    break
            word = self.words[word_index]

            if (self.hints - (self.words_length + 2)) % 2 == 0:
                word_letter = word[0]
                print(f'answer\'s word{word_index + 1} starts with \'{word_letter}\'')

            else:
                word_letter = word[-1]
                print(f'answer\'s word{word_index + 1} ends with \'{word_letter}\'')
            return True

    def hint_a_word(self):
        if 1 + 3 * self.words_length < self.hints < 2 + 4 * self.words_length:
            word_index = self.hints - 2 - 3 * self.words_length
            word = self.words[word_index]
            print(f"answer's word{word_index + 1} is {word}")
            return True

    def hint_help(self):
        hint = input("maybe a hint would help? y/n")
        if hint == 'y':
            self.hints += 1
            if self.hint_the_word_size_of_the_sentence(): return
            if self.hint_the_letter_size_of_a_word(): return
            if self.hint_the_edges_of_a_word(): return
            if self.hint_a_word(): return
            print("sorry, out of clues")

    def play(self):
        while True:
            bunny = input("bunny, please guess my message, your piggy =)")
            if bunny == self.guess:
                self.guess_is_correct()
                return
            else:
                self.tries += 1
                print("sorry, incorrect answer")
                yn = input("try again? y/n")
                if yn == 'n':
                    return
                else:
                    self.hint_help()


if __name__ == "__main__":
    game = GuessGame()
    game.play()

