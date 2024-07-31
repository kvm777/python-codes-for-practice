l = [0,3,2,5,6,2,5,6]

l1 = []
for i in l:
    if i>0:
        l1.append(True)
    else:
        l1.append(False)

print(l1)

# print(all([i>=0 for i in l]))

print(all(l1))
print(any(l1))

