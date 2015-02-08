

from icalendar import Calendar, Event
import urllib2



def test():
    url = 'https://www.google.com/calendar/ical/events%40a2geeks.org/public/basic.ics'
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    data = response.read()

    cal = Calendar.from_ical(data)

    for event in cal.walk('vevent'):
        print event
