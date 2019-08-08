import requests


def add(a, b):
    try:
        sum = a + b
        if not isinstance(sum, int) or not isinstance(sum, float):
            raise TypeError
    except TypeError:
        sum = float(a) + float(b)
    print(sum)


add(1, 3)
add(5, 6)
add('5', 2)
add('1', '2')


class KeepAliveException(Exception):
    pass


def url_keep_alive():
    try:
        r = requests.get('http://www.invalidurl.net4u')
        print(r.text)
    except requests.exceptions.ConnectionError:
        print('this url is invalid')
        try:
            r = requests.get('https://web.whatsapp.com/')
            print(r.text)
        except:
            raise KeepAliveException('you tried to handle an invalid url connection error but you failed')


try:
    url_keep_alive()
except KeepAliveException:
    print(KeepAliveException)


from qaviton.utils.databases.sqlite import DataBase
db = DataBase('database')
r = db.execute('''CREATE TABLE contacts (
 contact_id integer PRIMARY KEY,
 first_name text NOT NULL,
 last_name text NOT NULL,
 email text NOT NULL UNIQUE,
 phone text NOT NULL UNIQUE
);''')
print(r)
try:
    db.close()
except:
    pass


def devide(a, b):
    if a > 100:
        raise ValueError('does not support devision of numbers bigger than 100')
    else:
        return a/b


a = 100
b = 0
try:
    devide(a, b)
except ZeroDivisionError as e:
    b += 1
    print(devide(a, b))
except ValueError as e:
    if a > 100:
        a = 100
        if b == 0:
            print(1)
        else:
            print(devide(a, b))



