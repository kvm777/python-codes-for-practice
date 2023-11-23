class A():
    a = 10
    def fun1(self):
        print(20)

class B(A):
    b = 30
    def fun2(self):
        print(40)

class C(B):
    c = 50
    def fun3(self):
        print(60+self.b)

obj = C()
print(obj.a)
obj.fun1()
print(obj.b)
obj.fun2()
print(obj.c)
obj.fun3()
