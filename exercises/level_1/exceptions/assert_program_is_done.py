import time


class UserQuit(Exception):
    pass


def ask_user(question):
    try:
        choice = input(question + " [y,n,q]: ")
    except EOFError:
        raise UserQuit
    if choice.upper() in ['Y', 'YES', 'N', 'NO']:
        return choice.upper()[0]
    elif choice.upper() in ['Q', 'QUIT']:
        raise UserQuit
    return ask_user(question)


def assert_program_is_done():
    try:
        t = time.time()
        answer = ask_user('are you done yet?')
    except UserQuit:
        print("user has quit the program before it has asserted it's completion")
    else:
        t = time.time() - t
        if answer == 'Y':
            print('only took you {}sec'.format(t))
        elif answer == 'N':
            print('better luck next time')
    finally:
        print('assertion is done')


assert_program_is_done()
