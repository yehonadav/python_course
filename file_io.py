# coding=utf-8

filename = 'file'
# w=write a=append r=read x=create +=add read/write permissions
modes = ('w', 'a', 'r', 'x', 'x+', 'w+', 'a+', 'r+')
# ''=text b=binary t=text
formats = ('', 'b', 't')

for m in modes:
    for f in formats:
        if m.startswith('x'):
            try:
                open(filename, m + f).close()
            except FileExistsError:
                pass
        else:
            open(filename, m+f).close()


import requests


f = open(filename, 'w')
f.write(requests.get('https://www.w3schools.com/python/python_file_open.asp').text)
f.close()


with open(filename) as f:
    w3schools = f.readlines()


for line in w3schools:
    print(line)


with open(filename) as f:
    print(f.read(5))
    print(f.readline())
    print(f.readline())
    for line in f:
        print(line)


f = open(filename, 'w')
f.write('file content deleted')
f.close()

f = open(filename, "a")
f.write("file content + this line")

# מחיקת קובץ
import os
os.remove(filename)

if os.path.exists(filename):
    os.remove(filename)
else:
    print(filename + " does not exist")

# מחיקת תיקייה
if os.path.exists("myfolder"):
    os.rmdir("myfolder")
