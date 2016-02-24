class static_demo(object):
    class_param = 100

    def __init__(self):
        print "static method example"

    @staticmethod
    def add(a,b):
        """
        :param a: this value 1
        :param b: this value 2
        :return: adding of two value
        it does not depend on any self or class object
        """
        print static_demo.class_param
        # print self.__class__.class_param
        return a+b

    # def test():
    #     print "clarifications"

obj = static_demo()
o = obj.add(1, 20)
c = static_demo.add(20,40)

# obj.test()
# static_demo.test()

print o
print c

