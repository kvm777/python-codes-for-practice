# def add(a, *b):
#     s = a
#     for i in b:
#         s+=i
#     print(s)



# add(2,3,5,3,4,6,8,4)



#method overriding...

class A:
    def run(self):
        return "walk"
    
class B(A):
    def run(self):
        return "run"



obj1 = A()
obj2 = B()
print(obj1.run())
print(obj2.run())





