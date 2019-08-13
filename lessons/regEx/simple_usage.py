import re
from lessons.regEx import data


def use_iterator_of_matches(regex):
    """
    find matches for regex pattern
    iterate and print them
    save last match
    show last match span & value
    """
    matches = 0
    pattern = re.compile(regex)
    last_match = None
    for match in pattern.finditer(data):
        matches += 1
        last_match = match

    print('\n\nfound', matches, 'matches for', regex)
    if last_match:
        s1, s2 = last_match.span()  # last span start, stop
        print('last match:', last_match)
        print('regex value:', data[s1:s2])


if __name__ == '__main__':
    # find all `123` occurrences
    use_iterator_of_matches(r'123')

    # find any single character except \n
    use_iterator_of_matches(r'.')

    # find all `.` occurrences
    use_iterator_of_matches(r'\.')

    # find `qaviton.com`
    use_iterator_of_matches(r'qaviton\.com')

    # find all website occurrences
    use_iterator_of_matches(r'[a-zA-Z0-9_.]+\.[a-z]+')

    # find email occurrences
    use_iterator_of_matches(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')  # why only 3
