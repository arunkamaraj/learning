class A(object):
    var = 10
    def __init__(obj,f):
        obj.var_f = f
        print "constructor"
    def fun(obj):
        print "summa"

class B(A):
    var = 20
    def __init__(obj,g):
        obj.var_g = g
        print "B constructor"

if __name__ == "__main__":
    o = A(10)
    print o.var_f

    print A
    print o
    print A.fun
    print o.fun
