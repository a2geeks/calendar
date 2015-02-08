#!/usr/bin/env python
#
# Happenings Calendar Publisher
# Ryan Burns
#

import os
import logging
from argparse import ArgumentParser
from pprint import pprint, pformat

from happenings import gcal

try:
    import yaml
except ImportError:
    print "You must install PyYAML to use this script."
    print "Try pip install PyYAML"
    sys.exit(1)


def main(args):

    gcal.get_calendar()


#    with open(args.yaml_fn, 'r') as f:
#        conf = yaml.load(f)
#    logging.debug(pformat(conf))



if __name__ == '__main__':
    parser = ArgumentParser(description="Happenings Calendar Publisher")
    parser.add_argument("yaml_fn", help="YAML file containing configuration.")
    parser.add_argument("-d","--dryrun",action="store_true",default=False,
                      help="Will not publish anything.")
    args = parser.parse_args()

    main(args)

    root = logging.getLogger()
    root.setLevel(logging.INFO)

    fh = logging.FileHandler('happenings.log')
    fh.setLevel(logging.DEBUG)
    root.addHandler(fh)
