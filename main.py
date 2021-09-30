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

# read the webpage
if len(sys.argv) != 2:
    print('Usage:', sys.argv[0], '<URL>')
    sys.exit(1)

url = sys.argv[1]

response = urllib.request.urlopen(url)
html = response.read().decode('utf-8')

# find the number
m = re.search('<span id="profile--id-card--highlight-tooltip--karma" class="_1hNyZSklmcC7R_IfCUcXmZ">(.+?)</span>', html)
if m:
    print(m.group(1))
else:
    print('No match!')

