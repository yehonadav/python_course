from exercises.level_1.modules_and_packages import mdl as m

print(dir(m))
print(m.__name__.rsplit('.', 1)[-1])
