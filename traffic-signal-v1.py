#!/usr/bin/env python

import requests
import time
from datetime import datetime

def loadURL(url):
    contents = ''
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    return requests.get(url, headers=headers).content.strip()

if __name__ == "__main__":
    siglat = 21.3970
    siglon = -157.73923
    data = loadURL('http://roen.us/wapps/dev/evn/evn.txt')
    fields = data.split()
    evtime = int(fields[0])
    evtype = fields[1]
    evlat = float(fields[2])
    evlon = float(fields[3])

    dlat = siglat-evlat
    dlon = siglon-evlon

    distance = (dlat**2.0 + (0.93106 * dlon)**2.0)**0.5*111000.0

    now = datetime.now()
    inow = now.strftime("%s")
    iinow = int(inow)

    dtime = iinow-evtime


    print dtime, evtype, dlat, dlon
    print "Approximately", "%.1f" % distance, "meters"
    pass
