s=input()
l=s[-1]
if l in '0123456789':
    print(len(s)-1)
else:
    if len(s)>10:
        print(-1)
    else:
        print(len(s))