#max and min k values from tupple

def getk(t,k):
    l=list(t)
    l.sort()
    l=l[:k]+l[len(l)-k:]

    print(tuple(l))


tup=(5,33,53,6,3,6,34,64,65,3,6)
k=3
getk(tup,k)

#output : (3, 3, 5, 53, 64, 65)