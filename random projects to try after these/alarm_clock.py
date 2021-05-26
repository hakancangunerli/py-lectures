from datetime import datetime 
from playsound import playsound 


def validate_time(alarmtime):
  if len(alarmtime) != 11: 
    return "not a valid time"
  else:
    # slice the input, check if it's missing 
    if int(alarmtime[0:2]) > 12:
      return "hour is wrong"
    elif int(alarmtime[3:5]) > 59:
      return "minute is wrong"
    elif int(alarmtime[6:8]) > 59:
      return "second is wrong"
    else:
      return "successful"
  
  

while True:
  alarmtime = input("Insert time here: ")
  validate = validate_time(alarmtime.lower())
  if validate != "successful":
    print(validate)
  else: 
    print("setting alarm for", alarmtime)
    break 



# string is a list for characters 
'''
hello 
a = 'h'
b  = 'e'... 
String = list for character 
str hello 
str[0:2]
'''

# hr, min, sec, period[am/pm]
hour = alarmtime[0:2]
minute= alarmtime[3:5]
second = alarmtime[6:8]
period= alarmtime[9:].upper()

while True:
  now = datetime.now() 
  current_hour = now.strftime("%I")
  # s= s, m= m, p is for am/pm 
  current_min = now.strftime("%M")
  current_sec = now.strftime("%S")
  current_period = now.strftime("%p")

  if period == current_period:
    if hour == current_hour:
      if minute == current_min:
        if second == current_sec:
          print("All done!")

       
          