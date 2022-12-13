def opteller(a, b):
    try:
        answer = int(a) + int(b)
        print (answer)
    except ValueError:
        print("Please enter a number")

opteller(4,5)
