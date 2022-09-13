import psutil
import time
#from datetime import datetime, timedelta
#time = input("How long do you want to check the RAM (in seconds) ")
while True:
    plotter = ("#" * int(psutil.virtual_memory().percent), psutil.virtual_memory().percent)
    time.sleep(0.75)
    print (plotter)
