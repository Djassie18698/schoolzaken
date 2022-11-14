def checkLengtStringInList (): 
    lengte = int(input("Hoeveel letters mogen er maximaal in de string zitten? "))
    list = ["Hello", "World", "in", "a", "frame"] 
    for word in list: 
        if len(word) != lengte: 
            print(word)

checkLengtStringInList()