class encapsulation(object):
    __a = 1000
    _b = "Fuck"
    def data(self):
        self.__a += 1
        print "Acceessing as a instance variable ", self.__a
        print "Accessing as class variable", encapsulation.__a
        # print encapsulation.__a

class confusing():
    a = 1000
    def data(self):
        self.a += 1
        print "Acceessing as a instance variable ", self.a
        print "Accessing as class variable", confusing.a

if __name__ == "__main__":

    obj = encapsulation()
    obj.data()
    obj.data()
    print "From outside :", obj._encapsulation__a
    print "From outside :", obj._b
    obj._b = "Fuck u"

    print "From outside :", obj._b
    print "From outside as a class :", encapsulation._b

    print "--------------------------------------"

    obj = confusing()
    obj.data()
    obj.data()
    print "From outside :", confusing.a

