import shutil
import os


filename = 'myfile'


def exercise1():
    if os.path.exists(filename):
        os.remove(filename)
    else:
        open(filename, 'w').close()
    file = open(filename, 'a')
    file.write('1234567890')
    file.close()

    file = open(filename)
    content = file.read()
    file.close()
    print(content)


def exercise2():
    file = open(filename, 'a')
    file.writelines([
        '1, 11, 111, 1111, 11111\n',
        '2, 22, 222, 2222, 22222\n',
        '3, 33, 333, 3333, 33333\n',
        '4, 44, 444, 4444, 44444\n',
    ])
    file.close()
    file = open(filename)
    content10 = file.read(10)
    line1 = file.readline()
    line2 = file.readline()
    linesn = file.readlines()
    print('content10', content10)
    print('line1', line1)
    print('line2', line2)
    print('linesn', linesn)


def exercise3():
    dirname = 'mydir'
    with open(filename, 'a') as f:
        f.write('\n12345677')

    # handle dir exist error
    i = 0
    new_dirname = dirname
    while os.path.exists(new_dirname):
        new_dirname = dirname + str(i)
        i += 1

    filename_copy = filename + '_copy'
    new_dirname_copy = new_dirname + '_copy'
    moved_file = new_dirname+'\\'+filename

    os.mkdir(new_dirname)
    shutil.copyfile(filename, filename_copy)
    os.rename(filename, new_dirname+'\\'+filename)
    shutil.copytree(new_dirname, new_dirname_copy)

    print('files under new copied dir:', os.listdir(new_dirname_copy))

    os.remove(filename_copy)
    os.remove(moved_file)
    os.rmdir(new_dirname)
    shutil.rmtree(new_dirname_copy)
    print('all files and folders have been removed')


if __name__ == "__main__":
    exercise1()
    exercise2()
    exercise3()
