'''
a leap year is defined... if an year divided by 4 or divided by 400 and... if not divided by 100

'''

n=int(input())

if n%4==0:
    if n%100==0:
        if n%400==0:
            print("leap")
        else:
            print("not")
    else:
        print('leap')
else:
    print("not")


