'''
a leap year is defined... if an year divided by 4 or divided by 400 and... if not divided by 100

'''

n=int(input())

# if n%4==0:
#     if n%100==0:
#         if n%400==0:
#             print("leap")
#         else:
#             print("not")
#     else:
#         print('leap')
# else:
#     print("not")


if((n%4==0 and n%100!=0) or (n%100==0 and n%400==0)):
    print("leap year")
else:
    print("not a leap year")


    