def opteller():
    try:
        input1 = int(input("Geef een getal: "))
        input2 = int(input("Geef een tweede getal: "))
        input3 = str(input2+input1)
        print(input3)
    except ValueError:
        print("Please enter a number")