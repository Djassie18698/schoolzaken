import psutil
from datetime import datetime, timedelta
time = input("How long do you want to check the RAM (in seconds) ")

# Make a list for ram usage, divide ram usage total by entries made in the list
def average_ram_usage(time):
    start = datetime.now()
    end = start + timedelta(seconds=time)
    ram_usage = []
    while datetime.now() < end:
        ram_usage.append(psutil.virtual_memory().percent)
    return sum(ram_usage)/len(ram_usage)

print(average_ram_usage(int(time)))



