from clock import *
from alarm import *
from time import sleep
from datetime import datetime

setAlarm=checkAlarm()
while True:
    sleep(0.61)
    d = datetime.now()
    hour = int(datetime.now().strftime("%#I"))
    amPm = datetime.now().strftime("%p")
    printTime(hour, d.minute, d.second, amPm)
    drawClock(hour, d.minute, d.second)
    checkTime(setAlarm[0],setAlarm[1],setAlarm[2],hour, d.minute, amPm)
    