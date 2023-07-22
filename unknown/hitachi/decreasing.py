n=int(input())
c=0
for i in range(n+1):
    x=[int(j) for j in str(i)]
    if sorted(x,reverse=True)==x:
        c+=1
print(c)



