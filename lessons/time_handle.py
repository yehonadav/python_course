"""The datetime module supplies classes for
manipulating dates and times in both simple and complex ways.
While date and time arithmetic is supported, the focus
of the implementation is on efficient attribute extraction
for output formatting and manipulation.
For related functionality, see also the time and calendar modules.

There are two kinds of date and time objects: “naive” and “aware”.

An aware object has sufficient knowledge 
of applicable algorithmic and political time adjustments, 
such as time zone and daylight saving time information, 
to locate itself relative to other aware objects. 
An aware object is used to represent a specific moment in time 
that is not open to interpretation. 

A naive object does not contain enough information 
to unambiguously locate itself relative to other date/time objects. 
Whether a naive object represents Coordinated Universal Time (UTC), 
local time, or time in some other timezone is purely up to the program, 
just like it is up to the program whether a particular number represents 
metres, miles, or mass. Naive objects are easy to understand and to work with, 
at the cost of ignoring some aspects of reality.

For applications requiring aware objects, 
datetime and time objects have an optional time zone information attribute, 
tzinfo, that can be set to an instance of a subclass of the abstract tzinfo class. 
These tzinfo objects capture information about the offset from UTC time, 
the time zone name, and whether Daylight Saving Time is in effect. 
Note that only one concrete tzinfo class, the timezone class, is supplied by the datetime module. 
The timezone class can represent simple timezones with fixed offset from UTC, 
such as UTC itself or North American EST and EDT timezones. 
Supporting timezones at deeper levels of detail is up to the application. 
The rules for time adjustment across the world are more political than rational, 
change frequently, and there is no standard suitable for every application aside from UTC.
"""

import datetime
import calendar
import time

# year-month-day object
d = datetime.date(2016, 7, 24)
print(d)

today = datetime.date.today()
print(today)
print(today.day)
print(today.year)
print(today.weekday())  # monday=0 sunday=6
print(today.isoweekday())  # monday=1 sunday=7

deltime = datetime.timedelta(days=7)
print(today + deltime)  # future date
print(today - deltime)  # past date

birthday = datetime.date(2019, 10, 26)
time_until_birthday = birthday - today
print(time_until_birthday)
print(time_until_birthday.days)
print(time_until_birthday.total_seconds())

# hour-min-sec-mic object
t = datetime.time(9, 30, 45, 50000)
print(t)


# datetime object
dt = datetime.datetime(2018, 8, 26, 12, 30, 11, 30000)
print(dt)
print(dt.date())
print(dt.time())
print(dt.year)
print(dt.second)


deltime = datetime.timedelta(days=7)
print('next week', dt+deltime)

dt_today = datetime.datetime.today()
dt_now = datetime.datetime.now()
dt_utcnow = datetime.datetime.utcnow()
print(dt_today)   # current local datetime with no timezone
print(dt_now)     # current local datetime with optional timezone
print(dt_utcnow)  # current local utc datetime with optional timezone

# if you want timezones: pip install pytz
try:
    import pytz
    dt = datetime.datetime(2015, 7, 12, 30, 45, tzinfo=pytz.UTC)
    dt_utcnow = datetime.datetime.now(tz=pytz.UTC)
    print(dt)
    print(dt_utcnow)

    # pytz.all_timezones
    dt_me = dt_utcnow.astimezone(pytz.timezone("Israel"))

    # naive datetime object
    me_unaware = datetime.datetime.now()

    metz = pytz.timezone("Israel")
    me_aware = metz.localize(me_unaware)

    # show me datetime with other formats: https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior
    # convert datetime object into string
    print(dt_me.strftime('%B %d, %Y'))

    # convert string format into a datetime object
    time_format_string = 'July 26, 2016'
    dt = datetime.datetime.strptime(time_format_string, '%B %d, %Y')

    # convert datetime to epoc time
    epoc = datetime.datetime(2012, 4, 1, 0, 0).timestamp()

    # convert epoc to datetime
    dt = datetime.datetime.fromtimestamp(epoc)
    dt = datetime.datetime.utcfromtimestamp(epoc)
    print(epoc, dt)

except ImportError:
    print('missing module pytz is required for time aware objects')


# epoc time

epoc = time.time()
print('sleep 2 seconds')
time.sleep(2)
print('im awake')

print('representing time as  gmtime or localtime string', time.asctime())
print('current processor time as a floating point number expressed in seconds', time.clock())



# calender
print(calendar.weekheader(1))
print(calendar.weekheader(2))
print(calendar.weekheader(3))
print(calendar.weekheader(5))

print(calendar.firstweekday())  # first day is 0
print(calendar.month(2019, 3))  # calender of the month
print(calendar.monthcalendar(2019, 6))  # 2d array of the month
print(calendar.calendar(2019))  # calender of the year
print(calendar.weekday(2019, 6, 8))  # day of the week (num 0-6)
print(calendar.isleap(2020))  # is a leap year (feb -1 day every 4 years)
print(calendar.leapdays(2020, 3000))  # how many leaps




