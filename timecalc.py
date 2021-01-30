#!/usr/bin/env python3

import datetime
import re
import requests
from bs4 import BeautifulSoup

# get start/end times from dumplog
dumplog = input("dumplog plz: ")
r = requests.get(dumplog.rstrip())
soup = BeautifulSoup(r.text, 'html.parser')
text = str(soup)
q = re.search(r'Game began (.*), ended (.*)\.', text)
sin = q.group(1)
ein = q.group(2)

# manual command line inputs
#
# sin = input("Start time: ")
# ein = input("Endin time: ")

s = datetime.datetime.fromisoformat(str(sin))
e = datetime.datetime.fromisoformat(str(ein))
d = e - s
days = d // datetime.timedelta(days=1)
d = d - datetime.timedelta(days=days)
hrs = d // datetime.timedelta(hours=1)
d = d - datetime.timedelta(hours=hrs)
mins = d // datetime.timedelta(minutes=1)
d = d - datetime.timedelta(minutes=mins)
secs = d.seconds

time = [days, hrs, mins, secs]
iso = ""
for u in time:
    if u == days and days == 0:
        continue
    if len(str(u)) == 1:
        iso += "0" + str(u)
    else:
        iso += str(u)
    if u == days:
        iso += " "
    elif u == hrs or u == mins:
        iso += ":"

print(f"Wallclock time: {iso}")
