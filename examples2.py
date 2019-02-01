from exercises.data import get_data
from examples import sort_names_with_addresses
import random

# נשתמש פונקציה של sort_names_with_addresses
# ונוסיף לרשימה מיקוד
# נהפוך את הלוגיקה החדשה לפונקציה נוספת
# נייצר פונקציה נוספת שיודעת להוציא מיקוד מהרשימה ולחבר אותו לסכום
# נדפיס את names_with_addresses
# נדפיס את names_with_addresses_and_postal
# נדפיס את postal_summary


def create_names_with_addresses_and_postal(names_with_addresses):
    names_with_addresses_and_postal = []
    for i in names_with_addresses:
        names_with_addresses_and_postal.append((
            i[0],
            i[1],
            str(random.randint(0, 10))+
            str(random.randint(0, 10))+
            str(random.randint(0, 10))+
            str(random.randint(0, 10))+
            str(random.randint(0, 10))
        ))
    return names_with_addresses_and_postal


def sum_up_postal_codes_to_a_fat_number(names_with_addresses_and_postal):
    postal = 0
    for i in names_with_addresses_and_postal:
        postal += int(i[2])
    return postal


names_with_addresses = sort_names_with_addresses(get_data(30))
names_with_addresses_and_postal = create_names_with_addresses_and_postal(names_with_addresses)
postal_sum = sum_up_postal_codes_to_a_fat_number(names_with_addresses_and_postal)

print(names_with_addresses)
print(names_with_addresses_and_postal)
print(postal_sum)
