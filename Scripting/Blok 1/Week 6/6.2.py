number = input("Vul een getal in: ")
odd = 0
even = 0

try:
    for i in number:
        if int(i) % 2 == 0:
            even += 1
        else:
            odd += 1
    print("Even: " + str(even))
    print("Odd: " + str(odd))
    print("Total: " + str(even + odd))
except ValueError:
    print("De invoer bevat foutieve tekens")