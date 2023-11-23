n=int(input())
b=bin(n)[2:]

print(b)

t= n
s=''
while t>0:
    s+=str(t%2)
    t = t//2
print(s[::-1])