from abc import ABC,abstractmethod

class Abclass(ABC):
    def print1(self,x):
        print("Passed value:",x)
    @abstractmethod
    def task(self):
        print("We are inside Absclass task")
class test_class(Abclass):
    def task(self):
        print("We are inside test_class task")
test_obj=test_class()
test_obj.task()
test_obj.print1(100)