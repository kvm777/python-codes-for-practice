#write your code here
n=str(n)
f=''
for i in range(len(n)):
    if i==(len(n)-1):
        f+=n[i]+('0'*(len(n)-i-1))
    else:
        f+=n[i]+('0'*(len(n)-i-1))+'+'

return f



