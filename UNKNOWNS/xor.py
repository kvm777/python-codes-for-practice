a,b,c=map(str,input().split())
n3=[]

"""
input: 10101101 XOR 11101001
output: 01000100
"""

for i in range(len(a)):
    if a[i]==c[i]:
        n3.append(str(0))
    else:
        n3.append(str(1))

r=''.join(n3)
print(r)
