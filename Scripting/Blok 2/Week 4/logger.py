import platform
import time
seconds = 1670406131.7583818
local_time = time.ctime(seconds)
import os

def bestandlog():
    bestand = open("Logbestand.txt", "w+")
    log = ["Datum/Tijd: " + local_time, "Gebruiker: " + os.getlogin(), "Scriptnaam: " + __file__, "OS: " + platform.system()]
    for i in log:
        bestand.write(""+i+ "\n")
        print (i)
    bestand.close()

    if i in log:
        print ("Dit is een log bestand. ")
    else:
        print ("ERROR")

bestandlog()