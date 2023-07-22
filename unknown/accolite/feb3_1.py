n=int(input())
a=list(map(int,input().split()))
def increasing_subarray(a,n):
    c=0
    out=[]
    t=0
    for i in range(len(a)):
        for j in range(i,len(a)):
            ar1=a[i:j+1]
            for k in range(len(ar1)-1):
                if ar1[k]>ar1[k+1]:
                    c+=1
            if (c<=1) and len(out)<len(ar1):
                out=ar1
                t=c
            c=0

    return len(out)-t



