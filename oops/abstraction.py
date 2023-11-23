from abc import *

class abstract():
    @abstractmethod
    def func1(self):
        None

class concrete(abstract):
    def func1(self):
        print("in concrete class")


obj  = concrete()
obj.func1()