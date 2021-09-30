#!/usr/bin/env python3

'''
Get a number from a website.
The number is inside a span element.

Example:
    <span id="profile--id-card--highlight-tooltip--karma" class="_1hNyZSklmcC7R_IfCUcXmZ">702</span>

Output:
    702

'''

import sys
import urllib.request
import re
import argparse
import time
import datetime
import os


# Get the url and the target csv log file.
parser = argparse.ArgumentParser(description='Get the karma from reddit.')
parser.add_argument('-u', '--url', required=True, help='Website url')
parser.add_argument('-o', '--output', required=True, help='Output file')
args = parser.parse_args()


# Get the number
response = urllib.request.urlopen(args.url)
html = response.read().decode('utf-8')

# find the number
m = re.search('<span id="profile--id-card--highlight-tooltip--karma" class="_1hNyZSklmcC7R_IfCUcXmZ">(.+?)</span>', html)
if m:
    print(m.group(1))
else:
    print('No match!')


# Save the number together with a timestamp.
# Write header if the file is empty.
if not os.path.isfile(args.output):
    with open(args.output, 'w') as f:
        f.write('timestamp,karma\n')

with open(args.output, 'a') as f:
    f.write('{},{}\n'.format(datetime.datetime.now().isoformat(), m.group(1)))
    print('Saved!')




