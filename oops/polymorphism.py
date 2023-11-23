class A():
    a = 10
    def fun1(self):
        print(20)

class B(A):
    b = 30
    def fun1(self):
        print(40)

obj = B()
obj.fun1()