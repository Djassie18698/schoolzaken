l1 = [1,2,3,4,5,6,7,8,9,12,100]
l2 = [5,6,5,7,8,9,0,11,12,12]

def list1():
    for i in range(len(l1)):
        if l1[i] not in l2:
            print(l1[i])

def list2():
    for j in range(len(l2)):
        if l2[j] not in l1:
            print(l2[j])

list1(), list2()