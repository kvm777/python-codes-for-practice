s=input()
n=len(s)
if len(s)>10:
    r=s[0]+str(n-2)+s[-1]
else:
    r=s
print(r)