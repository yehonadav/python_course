# https://docs.python.org/3/library/functions.html#__import__
# https://stackoverflow.com/questions/8663076/python-best-way-to-add-to-sys-path-relative-to-the-current-running-script
# https://stackoverflow.com/questions/2916374/how-to-import-with-import
# https://stackoverflow.com/questions/1707709/list-all-the-modules-that-are-part-of-a-python-package
# https://stackoverflow.com/questions/17344561/python-perform-relative-import-when-using-import
import os


print = lambda *args, **kwargs: print(*args, **kwargs, end="\n\n")


print("let's see the program's root directory:")
print(os.getcwd())

m1 = __import__('exercises', globals(), locals(), [], 0)  # import a package
print("importing package exercises as m1")

m2 = __import__('exercises.data', globals(), locals(), [], 0)  # import a sub module
print("importing sub module exercises.data as m2")

get_data = __import__('exercises.data', globals(), locals(), ['get_data'], 0)  # import function
print("importing function get_data from exercises.data")

m3 = __import__('exercises.data', globals(), locals(), ['*'], 0)  # import all
locals().update({k: getattr(m3, k) for k in dir(m3)})  # import all - update locals
print("importing * from exercises.data")


m4 = __import__('import_foo', globals(), locals(), [], 1)  # relative import: import .import_foo
print("relative import: .import_foo as m4", "m4.foo =", m4.foo)

foo = __import__('importing.import_foo', globals(), locals(), ["foo"], 2)  # relative import: from ..importing.import_foo import foo
print("relative import: from ..importing.import_foo import foo as foo", "foo =", m4.foo)

print("type(m1)", type(m1))
print("type(m2)", type(m2))

print("m1", m1)
print("dir(m2)", dir(m2))
print("m2.__file__", m2.__file__)


user1 = m2.data.get_data(1)
user2 = get_data(1)

print(type(get_data))
print(user1, user2)

print(m2.__path__)

import pkgutil

package = m1
p = package.__path__
subpackages = ["Found submodule %s (is a package: %s)" % (modname, ispkg) for importer, modname, ispkg in pkgutil.iter_modules(package.__path__)]
print('you can view subpackages in debug')
for p in subpackages:
    print(p)

