from logger import *

def writer():
    bestandlog()
    bestand = open("opdracht1week4.txt", "w")
    getallen = ['een', 'twee', 'drie', 'vier', 'vijf']
    for i in getallen:
        bestand.write("dit is regel "+i+"\n")
        print(i)
    bestand2 = open("logbestand.txt", "a")
    bestand2.write("regel wordt geprint")
    
def reader():
    bestand = open("opdracht1week4.txt", "r")
    for regel in bestand:
        print(regel, end = '')
    bestand.close()

print("Voorbeeld met schrijven van een file")
writer()    
print("... en teruglezen.")
reader()