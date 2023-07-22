def solution(message,key):
    s=message
    k=str(key)*(len(s)//2)
    a='abcdefghijklmnopqrstuvwxyz'
    l=[]
    for i in range(len(s)):
        l.append(str(a.index(s[i])+1+int(k[i])))

    l=','.join(l)

    return l








message=input()
key=int(input())

print(solution(message,key))