number = int(input("Vul een getal in boven de 0: "))
#geef een nummer in, dit nummer wordt vervolgens als variabele opgeslagen.
if number > 0:
    for x in range(number):
        x += 1 
        print("*" * x)
else:
    print("Het getal is niet boven de 0")