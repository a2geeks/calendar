

from icalendar import Calendar, Event
import urllib2

try:
    import pytz
except ImportError:
    print "Requires pytz"
    print "pip install pytz"
    sys.exit(1)



def test():
    url = 'https://www.google.com/calendar/ical/events%40a2geeks.org/public/basic.ics'
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    data = response.read()

    cal = Calendar.from_ical(data)

    for event in cal.walk('vevent'):
        date = event.get('dtstart').dt.astimezone(pytz.timezone('America/Detroit'))
        desc = event.get('description')
        summary = event.get('summary')
        location = event.get('location')
        print summary
        print desc
        print date
        print location
