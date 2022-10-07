x = input("Wat is het woord? ")
y = int(input("Wat is de stapgrootte? "))
z = list(x)
for x in range(y,len(z),y+1): # start from 3rd (index2) and step by y  
  z[x] = z[x].upper()
x = ''.join(z)
print (x)