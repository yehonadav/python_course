def hobbies(name, age: int, hobby, *optional_hobbies, **other):
    # enforce type
    if not isinstance(age, int):
        raise TypeError

    # handle optional hobbies
    oh = ''
    for i in optional_hobbies:
        oh += ' & ' + i

    # handle other content
    oth = ''
    for i in other:
        oth += ' {} {}'.format(i, other[i])

    return "my name is {}, my age is {}.\nI like to {}{}.{}"\
        .format(name, age, hobby, oh, oth)


if __name__ == "__main__":
    print(hobbies(
        'gob',
        30,
        'fly',
        'snow board',
        'porn',
        wood='i like to chop'
    ))
