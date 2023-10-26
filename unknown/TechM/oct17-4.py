def produtsAtNegativeTempreatures(tempreature):
    out = 0
    for i in tempreature:
        if i<0:
            out+=1

    return out



l = list(map(int,input().split()))
print(produtsAtNegativeTempreatures(l))

