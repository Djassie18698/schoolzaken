number = int(input("Vul een getal in boven de 0: "))

if number > 0:
    for i in range(1):
        for x in range(number):
            x +=1 
            print("*" * x)
else:
    print("Het getal is niet boven de 0")