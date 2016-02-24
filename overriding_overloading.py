class A(object):
    def __init__(self, a):
        self.a = 10
        # Trying for overloading
        self.x = self.value(a, 50)  # self.__class__.__name__ is B
        # and also self.__dict__ {'a': 10}

    def value(self, x, y):
        return "summa parent class function"

    @classmethod
    def test(cls, message):
        print "This is printed from base class", cls.__name__, message


class B(A):
    def __init__(self, a):
        self.a = a
        super(B, self).__init__(a)

    # overriding
    def value(self, data):
        return data

    # @classmethod
    def test(cls, message):
        super(B, cls).test(message)


o = B(20)
# B.test("hi")

# o = B(20)
# o.test("hi")