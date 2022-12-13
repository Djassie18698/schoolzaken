import platform
import time
from datetime import datetime
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
import os

def bestandlog():
    bestand = open("log.txt", "a")
    log = ["Datum/Tijd: " + current_time, "Gebruiker: " + os.getlogin(), "Scriptnaam: " + __file__, "OS: " + platform.system()]
    for i in log:
        bestand.write(""+i+ "\n")
        print (i)
    bestand.close()

    if i in log:
        print ("Dit is een log bestand. ")
    else:
        print ("ERROR")

