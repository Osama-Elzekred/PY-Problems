import pywhatkit as kit
from datetime import datetime

now = datetime.now()

chour = now.strftime("%H")
minutes = int(now.strftime("%M"))
# print(chour)
# print(minutes)
# print(minutes+1)
mobile = "+201094532662"
message = "مبعوت بالبايثون"
hour = int(chour) + int(input('Enter hour : '))
minute = int(input('Enter minute : '))
print(chour)
# help(kit.sendwhatmsg)

kit.sendwhatmsg(mobile,message,hour,minute)
# kit.playonyt('هزيم الرعد')
