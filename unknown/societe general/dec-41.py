
""""
input: n -> number of students
        1st line marks of one student..
        next followed lines of following lines..

output: find how many students get more marks than one student..

"""

n = int(input())

a = list(map(int,input().split()))
s = sum(a)
c = 0
for i in range(n-1):
    arr = list(map(int,input().split()))
    if sum(arr)>s:
        c+=1

print(c)



