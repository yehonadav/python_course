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

names_with_addresses = sort_names_with_addresses(get_data(30))

for i in range(len(names_with_addresses)):
    names_with_addresses[i] = (
        names_with_addresses[0],
        names_with_addresses[1],
        str(random.randint(0, 10))+
        str(random.randint(0, 10))+
        str(random.randint(0, 10))+
        str(random.randint(0, 10))+
        str(random.randint(0, 10))
    )
