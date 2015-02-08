#
# Google Calendar Event Acquisition
# Ryan Burns
#

import os
import sys
import httplib2

#GCal Imports:
try:
    from apiclient.discovery import build

except ImportError:
    print "You must have the Google API client library installed."
    print "pip install --upgrade google-api-python-client"
    sys.exit(1)


def get_api_key_from_env():
    EV = 'GOOGLE_HAPPENINGS_API_KEY'
    api_key = os.getenv(EV)
    if api_key is None:
        print "Did not find Google Calendar API Key environment variable " + EV
        sys.exit(1)
    return api_key


def get_calendar():
    api_key = get_api_key_from_env()
    cal = build('calendar', 'v3', developerKey=api_key)
