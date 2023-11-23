class A():
    __a = 10
    b = 20
    def __fun1(self):
        print("Private function")
    def fun2(self):
        print("public function")
        print(self.__a)
        return self.__fun1()
    

obj = A()
print(obj.b)
obj.fun2()