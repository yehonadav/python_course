from os import system, name
clear_screen = (lambda: system('cls')) if name == 'nt' else (lambda: system('clear'))
sep = ' '
end = '\n'
file = None

def render(*args, sep=sep, end=end, file=file):
    clear_screen()
    print(*args, sep=sep, end=end, file=file)

# test
# from time import sleep
# seq = (
#     '012',
#     '\n1',
#     '2',
#     '3',
#     '4',
#     '5',
#     '6',
#     '7',
#     '8',
#     '\n\n9'
# )
# new_lines = 0
# for i in seq:
#     render(i)
#     sleep(0.3)