class A:
    a = 10
    def __init__(self):
        print("constuctor is called when object is created")
        print(self.a)

    def fun1(self):
        print(20+self.a)
        
    def fun2(self, x):
        self.fun1()
        print(x+self.a)

obj = A()
print(obj.a)
# obj.fun1()
obj.fun2(10)



