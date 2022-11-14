def checkShortWordInString ():
    # Vraag een zin van de gebruiker
    woord = input("Geef een zin op: ")
    # hij kijkt welk woord van de zin het kortste is
    shortest = min(woord.split(), key=len)
    # hij zoekt de index op van het kortste woord
    index = woord.index(shortest)
    print("Het kortste woord is: ", shortest)
    print("Lengte: ", len(shortest))
    print("Index: ", index)

checkShortWordInString()