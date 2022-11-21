l1 = [1,2,3,4,5,6,7,8,9,12,100]
l2 = [5,6,5,7,8,9,0,11,12,12]

for x in range(len(l1)):
    if l1[x] in l2:
        print(l1[x])