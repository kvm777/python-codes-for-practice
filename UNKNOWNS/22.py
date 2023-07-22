def solution(string):  
    s=string.split()

    s1='abcdefghijklmnopqrstuvwxyz'
    s2='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    c=0
    for i in s:
        for j in i:
            if any(i.islower(j))==True:
                if i in s1:
                    c+=(s1.index(i)+1)

                if i in s2:
                    c=c+(s2.index(i)+1)
            else:
                if i in s1:
                    c+=(s1.index(i)+1)

                if i in s2:
                    c=c+(2(*(s2.index(i)+1)))


    return c

print(solution('abc ABC Abc'))

 
