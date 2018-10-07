##############
#   #   משתנים
##############

# ה                                                                                VAR הוא שם למשתנה
# 35 הוא ערך מספרי למשתנה VAR
var = 35

# ש                                                                         first_name הוא שם למשתנה
# ש                                                           'Yosi Dahan' הוא ערך מסוג UTF-8 למשתנה
# first_name למשתנה UTF-8 הוא ערך מסוג 'Yosi Dahan'
first_name = 'Yosi Dahan'

# ידפיס את הערך של VAR
print(var)

##############
# # הקצאת שמות
##############

MANAGERNAME = "אדם"
MANAGER_NAME = "אדם"
Manager_Name = "אדם"
ManagerName = "אדם"
managerName = "אדם"

# בפייתון לרוב נהוג להקצות שמות למשתנים בקונבנציה הבאה
manager_name = "אדם"

print(manager_name)

##############
#   #    חשבון
##############

number = 0
print(number)

# חיבור
number = number + 1
number += 1
print(number)

# חיסור
number = 4 - 1
number -= 1
print(number)

# כפל
number *= 2
number = number * 1
print(number)

# חילוק
number /= 2
number = number / 1
print(number)

# שימוש בסוגריים
number = (1 + 3) * 3 + 4 / 2
print(number)

# חזקות
number **= 2 ** 2
print(number)

# חלוקה עם שארית
number = number % 3
print(number)

# משתנה מסוג FLOAT (שבר)
print(10.5 / 9)

# המרת משתנים:  תווים,   שברים,   מספרים שלמים
print(int("1"), float(1), str(57.3))

# שורש
print(16 ** 0.5)

##############
#  #   מחרוזות
##############

# מחרוזות הן משתנה המתאר רצף של תווים
# (אותיות, מספרים וערכים שונים של ביטויים כמו רווח, סימן קריאה וכו')
# ההכרזה על משתנה מסוג מחרוזת נעשית באמצאות מרכאות או גרשיים
gutin1 = 'daniel gutin'
gutin2 = "daniel gutin"
gutin3 = '''
daniel 
gutin
'''
gutin4 = """
daniel 
gutin
"""
# מחרוזות ניתן לחבר כמו מספרים
print(gutin1 + gutin2 + gutin3 + gutin4)

full_name = gutin1 + "love or "
age = 23.7

# מחרוזות לא ניתן לחבר עם מספרים
try:
    name_and_age = full_name + age
except Exception as e:
    print(e, ":you can't add integers or floats to a string!")
    name_and_age = full_name + str(age)

# אבל ניתן להטמין פרמטרים במחרוזות
print("p1={}, p2={}, p3={}, p4={red}".format(1, 1.0, object(), red='#ff0000'))

# ירידת שורה n\
print("line 1 \n\n\n now im down 3 lines")

# TAB t\
print("def goku(attack):\n\tprint(attack)\n")

# בדיקה עם מחרוזת קיימת בתוך מחרוזת
print("אידן" in "אידן חכימי")

s1 = "012345"
# התו האחרון
print(s1[-1])

# התו הראשון
print(s1[0])

# כל התווים בין הראשון לאחרון
print(s1[1:-1])

##############
#   #   רשימות
##############
# כמו מחרוזות
# מאחסנות בתוכן רצף של איברים(מחרוזות, מספרים, שברים, וכו') במקום תווים

# הכרזה על רשימה
my_list1 = []
my_list2 = list()

# בניית רשימה
my_list3 = [0, 1.0, '3', []]

# חיבור רשימות
my_list4 = my_list3 + [77]

# הכפלת רשימות
my_list5 = my_list4*2

# בניית רשימה עם לולאה (למתקדמים)
my_list6 = [i for i in my_list5]

# בניית רשימה עם לולאה ותנאי (למתקדמים)
my_list7 = [i for i in my_list5 if isinstance(i, int)]

# בניית רשימה ממחרוזת
my_list8 = list("1234567")

# בניית מחרוזת מרשימה
my_string1 = ''.join(my_list8)

# המרת מחרוזת לרשימה
my_list9 = my_string1.split()

# שימוש בLEN לתאר את גודל הרשימה
print(len(my_list1))
# נשתמש בAPPEND בכדי להוסיף ערך לרשימה
my_list1.append(1)
my_list1.append(3)
my_list1.append(4)
my_list1.append(5)
print(len(my_list1))

# נשתמש בINSERT אם נרצה להוסיף ערך לרשימה במקום מסוים
# תמנעו מפעולה זו כיוון שהיא פוגעת בביצועים
my_list1.insert(1, 2)
print(my_list1)

# נשתמש בPOP בכדי להוציא ערך מהרשימה
pop1 = my_list1.pop(1)
# תמיד כדאי להוציא/להוסיף ערך לסוף הרשימה כדי לא לפגוע בביצועים
pop_last = my_list1.pop()
print(len(my_list1))
print(my_list1)

# נבדוק שערך קיים ברשימה
print("google" in ["tornado", "ocean", "hurikan", "google"])

# פנייה לאיברים מתוך הרשימה
print(pop1, pop_last, my_list1[0], my_list1[-1])


####################
#   #  רשימות קבועות
####################
# כמו רשימות
# מאחסנות בתוכן רצף קבוע של איברים שלא ניתן לשינוי
# חוסך במשאבים, משפר ביצועים

# הכרזה על רשימה קבועה - הכרזה על רשימה קבועה ריקה היא חסרת משמעות
my_tuple = tuple()

# בניית רשימה קבועה
my_tuple1 = (0, 1.0, '3', [])

# בניית רשימה קבועה ממחרוזת
my_tuple2 = tuple("1234567")

# שימוש בLEN לתאר את גודל הרשימה
print(len(my_tuple1))

# נבדוק שערך קיים ברשימה
print("3" in my_tuple2)

# פנייה לאיברים מתוך הרשימה
a = my_tuple1[0]
b = my_tuple2[1]
print(a, b)


####################
#     #      מילונים
####################
# כמו רשימות
# חיבור בין שם לערך ואחסון של זוגות שם:ערך
# בדומה ספר טלפונים או רשימת כתובות מגורים עם שם ומספר
# מתוארים גם כMAP וHASH TABLE

# הכרזה על מילון
my_dict1 = {}
my_dict2 = dict()

# בניית מילון
my_dict3 = {'int': 0, 'float': 1.0, 'str': '3', 'list': []}
my_dict4 = dict(ani='optimus', idan='mustard')

# חיבור מילון
my_dict5 = dict(my_dict3, **{'cool_number': 77})
my_dict6 = my_dict5.update(my_dict4)

# שימוש בLEN לתאר את גודל המילון
print(len(my_dict1))

# הוספת שם:ערך למילון
my_dict1['adi'] = '050-8507700'
my_dict1['nissan'] = '050-7658388'
my_dict1['bar'] = '054-5557787'
my_dict1['bob'] = '052-2253974'
print(len(my_dict1))

# מחיקת שם:ערך מהמילון
del my_dict1['adi']

# נבדוק ששם קיים במילון
print("adi" in my_dict1)

# נבדוק שערך קיים במילון
print("050-7658388" in my_dict1.values())

# פנייה לאיברים מתוך המילון
print(my_dict1["bob"], my_dict1['adi'])