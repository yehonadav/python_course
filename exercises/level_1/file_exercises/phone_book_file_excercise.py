import os


filename = 'phone_book.txt'

if not os.path.exists(filename):
    open(filename, 'w').close()

program_menu = """
========= Phone Book ========
   Please Select an Action

(1) add a new number
(2) show phone numbers

"""
user_choice = input(program_menu)
if user_choice not in '12':
    raise ValueError("Please Select a valid option (1 or 2)")

if user_choice == '2':
    file = open(filename)
    lines = file.readlines()
    file.close()
    lines_range = input("select lines start-stop, example:5-12")
    if lines_range == "":
        numbers = lines
    else:
        lines_range = lines_range.split('-')
        start = int(lines_range[0])
        stop = int(lines_range[1])
        if start > len(lines):
            start = 0
        if stop > len(lines):
            stop = len(lines)

        numbers = lines[start:stop]
    for number in numbers:
        print(number)
else:
    file = open(filename, 'a')
    new_phone_number = input("please enter a new phone number:")
    file.write(new_phone_number+'\n')
    file.close()
    print(f"phone {new_phone_number} added!")
