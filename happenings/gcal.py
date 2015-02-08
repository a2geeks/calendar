#
# Google Calendar Event Acquisition
# Ryan Burns
#

import os
import httplib2

#GCal Imports:
try:
    from apiclient.discovery import build
except ImportError:
    print "You must have the Google API client library installed."
    print "pip install --upgrade google-api-python-client"
    sys.exit(1)


def load_api_key():
    EV = 'GOOGLE_HAPPENINGS_API_KEY'
    api_key = os.getenv(EV)
    if api_key is None:
        print "Did not find Google Calendar API Key environment variable " + EV
    else:
        print "api_key", api_key
