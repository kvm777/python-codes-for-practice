a=input()       #input is always an mail..

if '@' in a:               #printing of gmail.com after mahesh@gmail.com
    a=list(a.split('@'))
    print(a[1])

else:
    print('invalid output')