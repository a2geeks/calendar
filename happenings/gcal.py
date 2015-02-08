#
# Google Calendar Event Acquisition
# Ryan Burns
#

import os

#GCal Imports:
try:
    from xml.etree import ElementTree
except ImportError:
    from elementtree import ElementTree
try:
    import gdata.calendar.data
    import gdata.calendar.client
    import gdata.acl.data
    import atom.data
except ImportError:
    print "You must have gdata installed to use cal command.  Try pip install gdata, or"
    print "see http://code.google.com/p/gdata-python-client/downloads/list"
    print "Tested with gdata 2.0.18"
    #Can continue with other commands



def load_api_key():
    EV = 'GOOGLE_HAPPENINGS_API_KEY'
    api_key = os.getenv(EV)
    if api_key is None:
        print "Did not find Google Calendar API Key environment variable " + EV
    else:
        print "api_key", api_key
