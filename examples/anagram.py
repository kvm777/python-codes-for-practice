#anagram code...

n1=input()
n2=input()

l1=set(n1)
l2=set(n2)

print(l1,l2)
print(sorted(n1),sorted(n2))

if sorted(n1)==sorted(n2):
    print("true")
else:
    print("false")