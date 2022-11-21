def main():
    getal = input("Welk getal wil je checken? ")
    if getal.isdigit():
        getal = int(getal)
        if getal % 2 == 0:
            print("Getal is even")
        else:
            print("Getal is oneven")
    elif getal != int():
        print("geen getal")
        

main()



