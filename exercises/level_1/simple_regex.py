import re
from regEx.data import sentences, data as regex_text
from exercises.data import create_user, get_data, get_data_as_text, transform_data_to_text
from exercises.level_1.hobbies import add_random_hobby, add_second_hobby
from qaviton.utils.helpers import funcname

sentences = ''.join(sentences)
user = create_user()
users10 = get_data(10)
users20 = get_data(20)

add_random_hobby(users20)
add_random_hobby(users10)
add_second_hobby(users10)

user = transform_data_to_text([user])
users10 = transform_data_to_text(users10)
users20 = transform_data_to_text(users20)
users30 = get_data_as_text(30)

combined_data = ''.join([sentences, user, users10, users20, users30, regex_text])


def find_matches(regex, string):
    pattern = re.compile(regex)
    return [match for match in pattern.finditer(string)]


def exercise_63(data):
    # print the number of matches for b-x + F-W or whitespace 0 times or more + 2-6
    matches = find_matches(r'[b-x]([F-W]|\s)?[2-6]', data)
    print(f'{funcname()} found {len(matches)} matches')


def exercise_64(data):
    # print the number of matches for exclusion any of these characters acegijlnprtvxz
    matches = find_matches(r'[^acegijlnprtvxz]', data)
    print(f'{funcname()} found {len(matches)} matches')


def exercise_65(data):
    # print the number of matches for any none word character or any of IDAN
    matches = find_matches(r'[^\w]|[IDAN]', data)
    print(f'{funcname()} found {len(matches)} matches')


def exercise_66(data):
    # print the number of matches for a/b/c + any character
    matches = find_matches(r'([abc].)|([abc]\n)', data)
    print(f'{funcname()} found {len(matches)} matches')


def exercise_67(data):
    # print the number of matches for any 5 characters
    matches = find_matches(r'(?:\w{5})', data)
    print(f'{funcname()} found {len(matches)} matches')


def exercise_68(data):
    # print the number of matches for all numbers
    matches = find_matches(r'\d+', data)
    print(f'{funcname()} found {len(matches)} matches')


def exercise_69(data):
    # Search the string to see if it starts with "name" and ends with "a number adn a white-space"
    # print the result
    match = re.search(r"^name.*\d\s$", data)
    if match is None:
        print(f'{funcname()} found no matches')
    else:
        print(f'{funcname()} found {match}')


def exercise_70(data):
    # print the number of matches of 'to'
    x = re.findall(r"to", data)
    print(f'{funcname()} found {len(x)} matches')


def exercise_71(data):
    # print 0 matches if no match was found for 'zombie'
    x = re.findall(r"zombie", data)
    print(f'{funcname()} found {len(x)} matches')


def exercise_72(data):
    # Search for the first white-space character in the string
    # print the result
    x = re.search(r"\s", data)
    if x is None:
        print(f'{funcname()} found no matches')
    else:
        print(f'{funcname()} found {x}')


def exercise_73(data):
    # Make a search that returns no match
    # print the result
    x = re.search(r"idan is stronger than yonadav", data)
    if x is None:
        print(f'{funcname()} found no matches')
    else:
        print(f'{funcname()} found {x}')


def exercise_74(data):
    # Split at each white-space character
    # print the number of matches
    x = re.split(r"\s", data)
    print(f'{funcname()} splited {len(x)} matches')


def exercise_75(data):
    # Split the string only at the first occurrence of a white-space
    # print the number of matches
    x = re.split(r"\s", data, 1)
    print(f'{funcname()} splited {len(x)} matches')


def exercise_76(data):
    # replace every white-space character with tab
    x = re.sub(r"\s", "\t", data)
    if x != data:
        print(f'{funcname()} replaced all white-spaces with a tab')
    else:
        print(f'{funcname()} could not find any white-spaces to replace')


def exercise_77(data):
    # replace the first 2 occurrences of a white-space to _
    x = re.sub(r"\s", "_", data, 2)
    if x != data:
        print(f'{funcname()} replaced 2 white-spaces with _')
    else:
        print(f'{funcname()} could not find any white-spaces to replace')


def exercise_78(data):
    # Do a search that will return a Match Object
    # print the match regex, string(text) size, span and value(match group)
    regex = r"qaviton"
    x = re.search(regex, data)
    if x is None:
        print(f'{funcname()} found no matches')
    else:
        print(f'{funcname()} found a match for \'{regex}\' in a {len(x.string)} size text: span={x.span()} value={x.group()}')


def exercise_79(data):
    # print the position (start- and end-position) of the first match occurrence.
    # The regular expression looks for any words that starts with a "na"
    x = re.search(r"\bna\w+", data)
    if x is None:
        print(f'{funcname()} found no matches')
    else:
        print(f'{funcname()} found a match at {x.span()}')


def exercise_80(data):
    # print the value of the first match match.
    # The regular expression looks for any words that starts with an "S"
    x = re.search(r"\bS\w+", data)
    if x is None:
        print(f'{funcname()} found no matches')
    print(f'{funcname()} found {x.group()}')


def exercise_81(data):
    # print the value of the first match.
    # The regular expression looks for any words that starts with an "S"
    # whats wrong here? make an error handler
    try:
        x = re.search(r"\bS\w+", str)
    except TypeError:
        x = re.search(r"\bS\w+", data)
    print(x.group())
    print(f'{funcname()} found {x.group()}')


def exercise_82(data):
    # print any word that starts with ar
    matches = find_matches(r'\bar\S*', data)
    print(f'{funcname()} found {len(matches)} matches')


def exercise_83(data):
    # print all matches of any characters with 2 following occurrences
    matches = find_matches(r'(.)\1\1', data)
    print(f'{funcname()} found {len(matches)} matches')


def exercise_84(data):
    # print the starting 2 characters of the sentence
    print(f'{funcname()} found {re.search(r"^..", data)}')


def exercise_85(data):
    # print the final 10 characters of the sentence
    print(f'{funcname()} found {re.search(r".{10}$", data)}')


def exercise_86(data):
    # print the number of matches for the following 3 a-z A-Z characters after each white-space
    matches = find_matches(r'\b[a-zA-Z]{3}', data)
    print(f'{funcname()} found {len(matches)} matches')


def exercise_87(data):
    # print the number of matches for all valid ip octets(0-255)
    matches = find_matches(r'\d+', data)
    valid_octats = 0
    for suspect in matches:
        if len(suspect.group()) < 4:
            if 0 <= int(suspect.group()) <= 255:
                valid_octats += 1
    print(f'{funcname()} found {valid_octats} matches')


def exercise_88(data):
    # print the number of matches for any single character except \n
    matches = find_matches(r'.', data)
    print(f'{funcname()} found {len(matches)} matches')


def exercise_89(data):
    # print the number of matches for all `.` occurrences
    matches = find_matches(r'\.', data)
    print(f'{funcname()} found {len(matches)} matches')


def exercise_90(data):
    # print the number of matches for all website occurrences
    matches = find_matches(r'[a-zA-Z0-9_.]+\.[a-z]+', data)
    print(f'{funcname()} found {len(matches)} matches')


def exercise_91(data):
    # print the number of matches for all email occurrences
    matches = find_matches(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', data)
    print(f'{funcname()} found {len(matches)} matches')


def exercise_92(data):
    # print set of the matches for all user names
    names = find_matches(r'name\: .*\n', data)
    names = {name.group()[6:-1] for name in names}
    print(f'{funcname()} found user names: {names}')


def exercise_93(data):
    # print set of the matches for all users first hobbies
    hobbies = find_matches(r'\nhobby\: .*\n', data)
    hobbies = {hobby.group()[8:-1] for hobby in hobbies}
    print(f'{funcname()} found users first hobbies: {hobbies}')


def exercise_94(data):
    # print set of the matches for all user hobbies
    hobbies = find_matches(r'\nhobby\: .*\n', data)
    hobbies = {hobby.group()[8:-1] for hobby in hobbies}

    hobbies2 = find_matches(r'\nsecond hobby\: .*\n', data)
    hobbies2 = {hobby.group()[15:-1] for hobby in hobbies2}

    hobbies.update(hobbies2)

    print(f'{funcname()} found users hobbies: {hobbies}')


def exercise_95(data):
    # print set of all ip occurrences
    regex = r'\d+\.\d+\.\d+\.\d+\.{0}'
    matches = find_matches(regex, data)
    ips = set()
    for match in matches:
        suspect_ip = match.group()
        octets = suspect_ip.split('.')
        ip_is_valid = True
        for octet in octets:
            if len(octet) < 4:
                if 0 <= int(octet) <= 255:
                    continue
            ip_is_valid = False
            break
        if ip_is_valid:
            ips.add(suspect_ip)
    print(f'{funcname()} found ip addresses: {ips}')
    
    
if __name__ == "__main__":
    # run the program in debug mode to assert each exercise
    exercise_63(combined_data)
    exercise_64(user)
    exercise_65(user)
    exercise_66(user)
    exercise_67(user)
    exercise_68(users20)
    exercise_69(users30)
    exercise_70(regex_text)
    exercise_71(user)
    exercise_72(regex_text)
    exercise_73(users20)
    exercise_74(user)
    exercise_75(user)
    exercise_76(user)
    exercise_77(user)
    exercise_78(regex_text)
    exercise_79(users10)
    exercise_80(regex_text)
    exercise_81(regex_text)
    exercise_82(combined_data)
    exercise_83(combined_data)
    exercise_84(sentences)
    exercise_85(sentences)
    exercise_86(sentences)
    exercise_87(combined_data)
    exercise_88(users30)
    exercise_89(users30)
    exercise_90(combined_data)
    exercise_91(combined_data)
    exercise_92(users30)
    exercise_93(users20)
    exercise_94(users10)
    exercise_95(combined_data)
