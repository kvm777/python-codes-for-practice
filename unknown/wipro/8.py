s=input()
x=input()
s=list(s)
for i in s:              #count of no of strs more than no.
    if x in s:
        s.remove(x)
s=''.join(s)
print(s)
