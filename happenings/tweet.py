#
# Ryan Burns
#

import os

try:
    from twitter import *
except ImportError:
    print "Requires twitter package."
    print "https://pypi.python.org/pypi/twitter"
    sys.exit(1)


def test(con_key, con_secret):

    print con_key
    MY_TWITTER_CREDS = os.path.expanduser('~/.my_twitter_credentials')
    if not os.path.exists(MY_TWITTER_CREDS):
        oauth_dance("A2Geeks Happenings", con_key, con_secret,
                    MY_TWITTER_CREDS)

    oauth_token, oauth_secret = read_token_file(MY_TWITTER_CREDS)

    twitter = Twitter(auth=OAuth(
            oauth_token, oauth_secret, con_key, con_secret))


    twitter.statuses.update(status='Hello, world!')
