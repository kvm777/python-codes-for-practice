n=int(input())
s1=str(n)
print(list(s1))
s=0
for i in s1:                 #su of odd digits code
    i=int(i)
    if i%2!=0:
        s+=i

print(s)