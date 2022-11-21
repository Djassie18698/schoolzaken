while True:
    check = input("Wat wil je checken? ")
    
    try:
        int(check)
        if int(check) < 0:
            print("De invoer bevat foutieve tekens")
    except ValueError:
        print("De invoer bevat foutieve tekens")
    else:
        print("")
    break