n=int(input())
l=list(map(int,input().split()))
li = []
count = 0
for i in l:
    if l.count(i)%2!=0 and i not in li:
        li.append(i)
        count+=1
print(count)