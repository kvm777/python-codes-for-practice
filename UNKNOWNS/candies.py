s=list(map(int,input().split()))

d=0
end=True

while end:
    s=sorted(s)
    s[2]=s[2]-1
    s[1]=s[1]-1
    s=sorted(s)
    d+=1
    if s[1]==0 and s[0]==0:
        end=False

print(d)

