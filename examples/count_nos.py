
#count the no of digits in string.....
# input: h5e3ll04ow87or33ld
# output: 8


a=input()

c=0
d=str(list(range(10)))  #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(d)
for i in a:
    if i in d:
        c+=1

print(c)


