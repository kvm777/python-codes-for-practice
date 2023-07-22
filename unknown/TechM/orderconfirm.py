def orderconfirm(orderID):
    n=str(orderID)
    r=1
    for i in n:
        r*=int(i)
    
    return r



x=int(input())
print(orderconfirm(x))
