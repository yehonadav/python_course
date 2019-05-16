import re
from regEx.data import data


def show_matches(regex):
    pattern = re.compile(regex)
    print('\n\n')
    for match in pattern.finditer(data):
        print(match)


if __name__ == '__main__':
    show_matches(r'.')
    # show_matches(r'\d')
    # show_matches(r'\D')
    # show_matches(r'\w')
    # show_matches(r'\W')
    # show_matches(r'\s')
    # show_matches(r'\S')

    # show_matches(r'\b')
    # show_matches(r'\B')
    # show_matches(r'^')
    # show_matches(r'$')
    #
    # # find a|b|c + any character except \n
    # show_matches(r'[abc].')
    # show_matches(r'[^abc]')
    # show_matches(r'[^\w]|[HBO]')
    # # find a/b/c + any character
    # show_matches(r'([abc].)|([abc]\n)')

    # find any 5 characters
    # show_matches(r'(?:\w{5})')

    # show_matches(r'\d+')
