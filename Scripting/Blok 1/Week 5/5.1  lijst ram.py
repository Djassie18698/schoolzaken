import psutil
import time
from datetime import datetime, timedelta

tijd = int(input("How long do you want to check the RAM (in seconds) "))
start = datetime.now()
end = start + timedelta(seconds=int(tijd))
lijst = []

while datetime.now() < end:
    time.sleep(1)
    lijst.append(int(psutil.virtual_memory().percent))
else:
    print (len(lijst))
    print (sum(lijst) / len(lijst))
    print (max(lijst))
    print (min(lijst))
