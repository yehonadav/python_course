from exercises.data import get_data

data = get_data(10)


for person in data:
    if person['age'] < 13:
        for k in person:
            print(k, person[k])
        break
else:
    print('all old people')
