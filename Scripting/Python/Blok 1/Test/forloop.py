'''
check = list(range(1, 101))

total1 = 0
for i in check:
    if i % 3 == 0 or i % 5 == 0:
        total1 += i

print(total1)
'''
invoer = int(input("tot welk getal wil je checken? "))
check = list(range(1, invoer+1))

total1 = 0
for i in check:
    if i % 3 == 0 or i % 5 == 0:
        total1 += i

if total1 > 50:
    print("Het getal is" ,total1)
    print("Dit is boven de 50")
else:
    print("Het getal is" ,total1)
    print("Dit is onder de 50")