import turtle
import winsound
setHour = int(input("Set a hour for the alarm: "))
setMinute = int(input("Set a minute for the alarm: "))
setamPm = str(input("am or pm: "))
def checkAlarm():
    if setHour < 12 or setHour >= 0:
        if setMinute < 60 or setMinute >= 0:
            if setamPm == 'am' or 'pm' or 'AM' or 'PM' or 'Am' or 'Pm' or 'aM' or 'pM':
                print(f"Alarm set to go off {setHour}:{setMinute} {setamPm.upper()}")
                return setHour, setMinute, setamPm
def checkTime(setHour, setMinute, setamPm,hour,minute,amPm):
    if setHour==hour  and setMinute==minute and setamPm==amPm.lower(): 
        winsound.PlaySound("sound.wav",winsound.SND_ASYNC)
        img = turtle.Screen()
        img.bgpic('hi.gif')
        print("Wake Up! Wake Up! Wake Up!")