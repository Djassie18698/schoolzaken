import psutil
from datetime import datetime, timedelta
time = input("How long do you want to check the RAM (in seconds) ")
current_time = datetime.now()
end_time = current_time + timedelta(seconds=float(time))

while current_time < end_time:
    ram_percent = psutil.virtual_memory().percent
    print("RAM percent: " + str(ram_percent) + "%")
    current_time = datetime.now()
if current_time > end_time:
    print (ram_percent/float(time))



