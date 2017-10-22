#!/usr/bin/python

from datetime import datetime
import time

import ftplib

def createData(vehicle, latitude, longitude):
    now = datetime.now()

    with open("evn.txt", "w") as f:
        f.write("%s %s %f %f\n" % (now.strftime("%s"), vehicle, latitude, longitude))
        pass
    
    ftp = ftplib.FTP("108.167.160.32")
    ftp.login("roenw@roen.us", "Aikahi16")
    ftp.cwd("/public_html/wapps/dev/evn")
    with open("evn.txt", 'r') as f:
        ftp.storlines("STOR evn.txt", f)
        pass
    ftp.quit()

if __name__ == "__main__":
    sltime=5
    deltaLo = (0.0076*sltime)/82.0
    deltaLa = -(0.013*sltime)/82.0

    vehicle = 'A'
    nbIterations = 50
    latitude = 21.410
    longitude = -157.74683

    while nbIterations > 0:
        createData(vehicle, latitude, longitude)
        latitude += deltaLa
        longitude += deltaLo
        nbIterations -= 1
        time.sleep(sltime)
