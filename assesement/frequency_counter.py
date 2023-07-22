
#INPUT: 8 8 1 1 3
#OUTPUT: 3 1 1 8 8             -------NOT DONE

l=list(map(int,input().split()))
d={}

for i in l:
    d[i]=l.count(i)

print(d)
