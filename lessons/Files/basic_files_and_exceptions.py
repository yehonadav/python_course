args = ['myfile.txt']

try:
    file = open(*args)
except FileNotFoundError:
    args.append('w')
    file = open(*args)

try:
    file.write('hello')
except Exception as e:
    print(e)
    file.close()
    args.append('a')
    file = open(*args)
    file.write('\nhello')
    file.writelines(['היי', "שלום"])
finally:
    file.close()

