from abc import ABC, abstractmethod
# abstract base class module
# abc is module
# ABC is class

# abstract class
class abstact(ABC):  
    @abstractmethod
    def fun1(self): 
        pass

    @abstractmethod
    def fun2(self):
        pass


# concete class
class concrete(abstact):
    def __init__(self):
        print("object is created")

    def fun1(self):
        return "fun1"
    def fun2(self):
        return "fun2"
    
obj = concrete()

print(obj.fun1())

