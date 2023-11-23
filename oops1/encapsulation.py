"""
priate ---  __varname, __funname() 
public --- varname, funname()


"""



class A:
    a = 10
    __b = 20

    def __privatefun(self):
        return "in private function"
    
    def fun1(self):
        print("in fun1")

        print("private varible ", self.__b)
        print(self.__privatefun())
        # return "in fun1"

obj = A()

print(obj.a)
# print(obj.__b)
obj.fun1()
# print(obj.fun1())
