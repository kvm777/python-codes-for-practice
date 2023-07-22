    
def vjsfnv(dataStream):
    l=dataStream
    s=l[0]
    f=''
    for i in s:
        i=i.lower()
        for j in range(1,len(l)):
            if i not in l[j]:
                break
        else:
            f+=i

    return f

    