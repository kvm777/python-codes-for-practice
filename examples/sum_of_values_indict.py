
#sum of values in dictionary

def dictsum(d):
    '''
    l=[]
    for i in d:
        l.append(d[i])
    s=0
    for e in l:
        s+=e

    print(s)
    '''
    sum=0
    for e in d.values():
        sum+=e
    print(sum)


dict={'a':100,'b':200,'c':300}
dictsum(dict)