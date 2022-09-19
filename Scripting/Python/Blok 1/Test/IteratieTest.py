lijst = ['Aan', 'Uit','Aan', 'Uit']
aantal = 0
zoekwoord = input("Welk woord zoek je?: ")
for woord in lijst:
    if woord == zoekwoord:
#Het aantal +=1 zegt eigenlijk aantal = aantal + 1, 
        aantal +=1
print("Het woord '{}', komt {} keer voor in de lijst.".format(zoekwoord,aantal))