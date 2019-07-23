import csv
import random
from exercises.data import get_data


def exercise1(filename, employees):
    with open(filename, mode='w') as employee_file:
        csv_file = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for employee in employees:
            csv_file.writerow(employee.values())


def exercise2(filename, employees):
    with open(filename, mode='w') as csv_file:
        csv_file = csv.DictWriter(csv_file, fieldnames=fieldnames)
        csv_file.writeheader()
        for employee in employees:
            csv_file.writerow(employee)


def exercise3(filename):
    with open(filename) as csv_file:
        csv_file = csv.reader(csv_file, delimiter=',')
        user_count = 0
        for row in csv_file:
            employee = {fieldname: fieldvalue for fieldname, fieldvalue in zip(fieldnames, row)}
            if len(employee):
                print(employee)
                user_count += 1
        print(f'Processed {user_count} employees.')


def exercise4(filename):
    with open(filename) as csv_file:
        csv_file = csv.DictReader(csv_file)
        user_count = 0
        for employee in csv_file:
            print(employee)
            user_count += 1
        print(f'Processed {user_count} employees.')


if __name__ == "__main__":
    employees = get_data(20)
    departures = ('IT', 'Accounting', 'Sales', 'Management', 'Research', 'Development', 'Testing', 'Integration')
    for employee in employees:
        employee['departure'] = random.choice(departures)

    fieldnames = employees[0].keys()
    csv_file_no_headers = 'employees1.csv'
    csv_file_with_headers = 'employees2.csv'

    exercise1(csv_file_no_headers, employees)
    exercise2(csv_file_with_headers, employees)
    exercise3(csv_file_no_headers)
    exercise4(csv_file_with_headers)

