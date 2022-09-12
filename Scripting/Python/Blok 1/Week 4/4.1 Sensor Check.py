import psutil
ramtotal = psutil.virtual_memory().total
ramused = psutil.virtual_memory().used
rampercent = psutil.virtual_memory().percent
battery = psutil.sensors_battery().percent
print ("RAM total: ", ramtotal)
print ("RAM used: ", ramused)
print ("RAM Percent ", rampercent,"%")
print ("Battery :", battery)