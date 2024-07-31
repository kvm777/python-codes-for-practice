a=input()       #input is always an mail..

if '@' in a:               #printing of gmail.com after mahesh@gmail.com
    # x=a.split('@')
    # print(x[1])
    i, j = a.split("@")
    print(j)

else:
    print('invalid output')