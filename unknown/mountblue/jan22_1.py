def solution(string):
    #write code here
    s=list(map(str,string.split()))
    a={}
    num='0123456789'
    for i in s:
        for j in range(len(i)):
            t=i[j]
            if t in num:
                a[t] = i[:j]+i[j+1:]

    f=''
    for i in sorted(a.keys()):
        f+=a.get(i)+" "

    return f

s=list(map(str,input().split()))
print(solution(s))


