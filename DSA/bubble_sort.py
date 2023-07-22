

#BUBBLE SORT

def bubblesort(l):
    for i in range(len(l)-1,0,-1):
        for j in range(i):
            if l[j]>l[j+1]:
                l[j],l[j+1]=l[j+1],l[j]
        
    print(l)

l=[20,40,600,70,30,650,50,80,60,90]
bubblesort(l)

