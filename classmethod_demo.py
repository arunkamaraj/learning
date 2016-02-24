# in class method it pass class as a first method 

def get_kls_no_class(class_object):
    print class_object.NO


def get_kls_no_instance(object):
    print object.__class__.NO

class kls(object):
    NO = 0
    def __init__(self):
        kls.NO = kls.NO + 1


class with_classmethod(object):
    roll_no = 0
    def __init__(self):
        with_classmethod.roll_no = with_classmethod.roll_no + 1

    @classmethod
    def get_rollno(cls):
        print cls.roll_no


print "With out class method implementation"
obj = kls()
obj1 = kls()
get_kls_no_class(kls)
get_kls_no_instance(obj1)

print "_____________________________________________\n"

print "With class method"
obj = with_classmethod()
obj1 = with_classmethod()
obj1.get_rollno()
with_classmethod.get_rollno()

# here we can call the class method with help of obj as well as class



