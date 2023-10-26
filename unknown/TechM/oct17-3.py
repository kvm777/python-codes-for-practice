def orderConformOtp(orderId):
    n = orderId
    out=1
    for i in str(n):
        out*=int(i)

    return out


n = int(input())
print(orderConformOtp(n))