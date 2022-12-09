import logging
from datetime import date
today = date.today()
print (today)

def logger():
    logging.basicConfig(filename="log.txt", level=logging.DEBUG)
    logging.info("Datum/tijd:", date.today())
    logging.info("Gebruiker: Jan Jansen")
    logging.info("Scriptnaam: ")
    logging.info("Operating System: 1.0")

logger()
