def evenorodd(getal):    
    try:
        if getal % 2 == 0:
            return("Getal is even")
        else:
            return("Getal is oneven")
    except ValueError:
        return("geen getal")
    except TypeError:
        return("geen getal")
    

if __name__ == '__main__':
    getal = input("Welk getal wil je checken? ")
    evenorodd(getal)
