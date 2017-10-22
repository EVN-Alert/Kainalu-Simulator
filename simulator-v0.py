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
    deltaLo = 0.001
    deltaLa = -0.001

    vehicle = 'A'
    nbIterations = 100
    latitude = 21.400
    longitude = -157.7365

    while nbIterations > 0:
        createData(vehicle, latitude, longitude)
        latitude += deltaLa
        longitude += deltaLo
        nbIterations -= 1
        time.sleep(10)
