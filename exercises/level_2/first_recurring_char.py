# go to the performance lesson "find_first_recurring_char_investigate_performance"
# to find out more about better solutions
def find_first_recurring_char(string):
    count = {}
    for char in string:
        if char in count:
            return char
        count[char] = 1


if __name__ == "__main__":
    print(find_first_recurring_char("abcdabcd"))
    print(find_first_recurring_char("abcd"))
