from ast import If
from collections import deque
import psutil
if psutil.virtual_memory().percent > 35:
   print("RAM usage is above 35%")