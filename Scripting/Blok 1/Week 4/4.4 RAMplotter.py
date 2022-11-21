import psutil
import time
from datetime import datetime, timedelta

tijd = int(input("How long do you want to check the RAM (in seconds) "))
start = datetime.now()
end = start + timedelta(seconds=int(tijd))

while datetime.now() < end:
    plotter = ("#" * int(psutil.virtual_memory().percent), psutil.virtual_memory().percent)
    time.sleep(0.5)
    print (plotter)   
