#import psutil
import psutil

#set values for ram and battery usage
ramtotal = psutil.virtual_memory().total
ramused = psutil.virtual_memory().used
rampercent = psutil.virtual_memory().percent
battery = psutil.sensors_battery().percent

#print set values
print ("RAM total: ", ramtotal)
print ("RAM used: ", ramused)
print ("RAM Percent ", rampercent,"%")
print ("Battery :", battery)