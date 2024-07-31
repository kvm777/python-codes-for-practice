# import pywhatkit
import pyAutoGui as p
import datetime

a = datetime.datetime.now()
min = a.minute
hours = a.hour
print(min, hours)


# pywhatkit.sendwhatmsg("+917569905899", "gvgvb", 11, 1)
# print("message sent")

# for i in range(10):
#     pywhatkit.sendwhatmsg("+917569905899", "gvgvb", hours, min+1)
#     print("message sent")
#     # time.sleep(10)

for i in range(20):
    p.typewrite("pawankalyan")
    p.press("enter")
