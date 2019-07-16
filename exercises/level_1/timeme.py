import datetime
import calendar
import time

now = datetime.datetime.utcnow()
last_year_date = datetime.date(now.year-1, now.month, now.day)
print('last year date', last_year_date)


today = datetime.date.today()
print('today date', today)
print('today', today.day)
print('today year', today.year)
print('today weekday', today.weekday())  # monday=0 sunday=6
print('today isoweekday', today.isoweekday())  # monday=1 sunday=7

deltime = datetime.timedelta(days=7)
print('next week', today + deltime)  # future date
print('last week', today - deltime)  # past date
print('the month of 5 weeks ago', (today - deltime*5).month)

birthday = datetime.date(2019, 10, 26)
time_until_birthday = birthday - today
print('time until birthday', time_until_birthday)
print('days until birthday', time_until_birthday.days)
print('seconds until birthday', time_until_birthday.total_seconds())
print('microseconds until birthday', time_until_birthday.total_seconds() * 1000000)


# hour-min-sec-mic object
timestamp = datetime.time(9, 30, 45, 50000)
print('datetime.time object timestamp', timestamp)
print('timestamp second', timestamp.second)
print('timestamp hour', timestamp.hour)
print('timestamp minute', timestamp.minute)
print('timestamp microsecond', timestamp.microsecond)


# datetime object
dt = datetime.datetime(today.year, today.month, today.day, 12, 30, 11, 30000)
print('datetime object dt', dt)
print('dt.date', dt.date())
print('dt.time', dt.time())
print('dt.year', dt.year)
print('dt.second', dt.second)


deltime = datetime.timedelta(weeks=52, days=1)
print('dt+deltime -> next year', dt+deltime)

dt1 = datetime.datetime.today()
dt2 = datetime.datetime.now()
dt3 = datetime.datetime.utcnow()
print('dt1', dt1)  # current local datetime with no timezone
print('dt2', dt2)  # current local datetime with optional timezone
print('dt3', dt3)  # current local utc datetime with optional timezone

# if you want timezones: pip install pytz
import pytz
dt4 = datetime.datetime(2015, 7, 17, 12, 30, 45, tzinfo=pytz.UTC)
dt5 = datetime.datetime.now(tz=pytz.UTC)
print('aware datetime object', dt4)
print('aware datetime object of now', dt5)

# pytz.all_timezones
dt6 = dt5.astimezone(pytz.timezone("Israel"))

metz = pytz.timezone("Israel")
dt7 = metz.localize(dt2)

# show me datetime with other formats: https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior
# convert datetime object into string
print('dt6.strftime timezone -> Israel', dt6.strftime('%B %d, %Y'))

# convert string format into a datetime object
time_format_string = 'July 26, 2016'
dt8 = datetime.datetime.strptime(time_format_string, '%B %d, %Y')

# convert datetime to epoc time
epoc = datetime.datetime(2012, 4, 1, 0, 0).timestamp()

# convert epoc to datetime
dt9 = datetime.datetime.fromtimestamp(epoc)
dt10 = datetime.datetime.utcfromtimestamp(epoc)
print('epoc, dt9, dt10', epoc, dt9, dt10)


# epoc time
epoc = time.time()
print('sleep 2 seconds')
time.sleep(2)
print('im awake')


# calender
print("the week headers with only 1 letter\n", calendar.weekheader(1), '\n')
print("the week headers with only 2 letters\n", calendar.weekheader(2), '\n')
print("the week headers with only 3 letters\n", calendar.weekheader(3), '\n')
print("the first day of the week", calendar.firstweekday())  # first day is 0
print("calendar of the 4th month of 1962", calendar.month(1962, 4), '\n')  # calender of the month
print("the 11th month of 2050 as a 2D list\n", calendar.monthcalendar(2050, 11), '\n')  # 2d array of the month
print("calendar of 2019\n", calendar.calendar(2019), '\n')  # calender of the year
print("the week day of today as a number 0-6", calendar.weekday(dt.year, dt.month, dt.day))  # day of the week (num 0-6)
print("if today's year is a leap year:", calendar.isleap(dt.year))  # is a leap year (feb -1 day every 4 years)
print("count of how many leap years are from today - year 3222:", calendar.leapdays(dt.year, 3222))  # how many leaps
