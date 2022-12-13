from logger import *

def writer():
    bestand = open("opdracht1week4.txt", "a")
    getallen = ['een', 'twee', 'drie', 'vier', 'vijf']
    for i in getallen:
        bestand.write("dit is regel "+i+"\n")
        print(i)
    bestand.close()
    bestand= open("log.txt", "a")
    bestand.write("regel wordt geprint \n")
    bestand.close()
    
def reader():
    bestand = open("opdracht1week4.txt", "r")
    for regel in bestand:
        print(regel, end = '')
    bestand.close()

bestandlog()
print("Voorbeeld met schrijven van een file")
writer()    
print("... en teruglezen.")
reader()