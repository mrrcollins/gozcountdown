#!/usr/bin/python3

import datetime as dt
import time

# Countdown date
cy=2020
cm=12
cd=22
chour=19
cmin=0

loop=100


while loop>0:
    start=dt.datetime.today()
    end=dt.datetime(cy,cm,cd,chour,cmin,00)

    t=end-start

    hours, remainder = divmod(t.total_seconds(), 3600)
    minutes, seconds = divmod(remainder, 60)

    line=str(int(hours)) +'H ' + str(int(minutes)) + 'M ' + str(int(seconds))+ 'S'
    loop=t.total_seconds()
    f = open("countdown.txt","w")
    f.write(line)
    f.close()
    time.sleep(1)
