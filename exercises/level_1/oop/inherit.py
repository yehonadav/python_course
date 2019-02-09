"""
This program illustrates the concept of inheritance
Python looks up for method in following order:
    instance attributes
    instance class attributes
    parent class attributes
    grand parent class attributes
    ...
"""
import time
import datetime


class Time:
    def get_time(self):
        return time.time()

class Date(Time):
    """Inheriting from Data class"""
    def get_date(self):
        return datetime.datetime.utcnow()

if __name__ == '__main__':
    date1 = Date()
    time1 = Time()

    print(time1.get_time())
    print(date1.get_time())  # Inherited
    print(date1.get_date())
