# inheritance...
"""
1.single level uinheritance
2.multi level inheritance
3. multiple inheritance
"""
class parent:
    a = 10
    def fun1(self):
        print("in fun1 parent class")
        print("a varible is ", self.a)

# single level inheritance
class child :
    b = 20    
    def fun2(self):
        print("in fun2 child class")

class grandchild(parent, child):    #multiple inheritance
    c = 30      
    def fun3(self):
        print("in fun3 grandchild class")   
    def fun4(self):
        return self.fun2()


obj = grandchild()
print(obj.a)
obj.fun4()

