from abc import ABCMeta, abstractmethod

# class Base(metaclass = ABCMeta):
class Base(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def name(self):
        return
    @abstractmethod
    def age(self):
        return

class Concrete(Base):
    def name(self):
        print "Arun"

    def age(self):
        print "25"

class incomplete_Concrete(Base):
    def name(self):
        print "Arun"


print "--------------- For concrete ----------------"
perfect_obj = Concrete()
perfect_obj.name()
perfect_obj.age()

isinstance(perfect_obj, Base)
issubclass(Concrete, Base)


print "---------- For Incomplete concrete ----------"


incom_obj = incomplete_Concrete()
incom_obj.name()
incom_obj.age()

isinstance(incom_obj, Base)
issubclass(incomplete_Concrete, Base)

