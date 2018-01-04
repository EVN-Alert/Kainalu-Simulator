#!/usr/bin/python

from datetime import datetime
import time

def createData(vehicle, latitude, longitude):
    now = datetime.now()

    with open("evn.txt", "w") as f:
        f.write("%s %s %f %f %s\n" % (now.strftime("%s"), vehicle, latitude, longitude, end))
        pass

    with open("evn.txt", 'r') as f:
        os.system('scp "%s" "%s:%s"' % (f, "roenus0j@az1-ss1.a2hosting.com", "/home/roenus0j/public_html/wapps/dev/evn/") )
        pass

if __name__ == "__main__":
    sltime=5
    deltaLo = (0.0076*sltime)/82.0
    deltaLa = -(0.013*sltime)/82.0

    vehicle = 'A'
    end = 'end'
    nbIterations = 50
    latitude = 21.410
    longitude = -157.74683

    while nbIterations > 0:
        createData(vehicle, latitude, longitude)
        latitude += deltaLa
        longitude += deltaLo
        nbIterations -= 1
        time.sleep(sltime)
