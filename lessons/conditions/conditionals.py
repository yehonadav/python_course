##################
#     #      תנאים
##################


from lessons.conditions_lessons.mail import mail
from time import sleep


def check_mail():
    if mail.new:
        new_mail = mail.get()
        print(new_mail)
    else:
        print("no new mails")


check_mail()

mail.send()
check_mail()

sleep(1)
mail.send()
check_mail()


def hack_mail():
    if mail.new == True:
        mail.get()
    elif not mail.new:
        mail.send()
        mail.new = 'banana'
    else:
        print('popcorn')


hack_mail()
hack_mail()


adi = dict(
    age=5,
    gender='male',
    power_level=9001)

sonny = dict(
    age=11,
    gender='female',
    power_level=7000)

if 0 < adi['age'] < 10:
    if adi['gender'] == 'male':
        print('bomb')
    elif adi['gender'] == 'female':
        print('blast')
    else:
        raise Exception('there are only 2 genders!')

if adi['power_level'] > sonny['power_level']:
    print('adi is stronger by {} levels'.format(adi['power_level']-sonny['power_level']))
else:
    print('adi has a long way to go')

if True:
    if True:
        if True:
            if True:
                print('indentation x 4')


