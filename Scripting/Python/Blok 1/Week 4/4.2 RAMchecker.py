from ast import If
from collections import deque
import psutil
import time

while psutil.virtual_memory().percent > 35:
   time.sleep(0.5)
   print("RAM usage is above 35%")
else:
   time.sleep(0.5)
   print("Ram usage is below 35%")
   