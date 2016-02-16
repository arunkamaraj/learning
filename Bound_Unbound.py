class ClassA():
    def f(self):
        print "Original Implementation"



obj = ClassA()
obj.f()

print ClassA.f  # it is not bounded
print obj.f  # it is bounded to the instance
# ClassA.f()
ClassA.f(obj)

#replacing other fuction to class
def second(self):
    print "Second Implement"

ClassA.f = second
obj.f()

#mapping function to class

print "mapping function to class"
g = second.__get__(obj,ClassA)
g()



ClassA().f()








