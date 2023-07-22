n=int(input())
l=[]
for i in range(n):
    l.append(input())


for i in l:
    if i[0]==i[-1]:
        print(True)
    else:
        print(False)


