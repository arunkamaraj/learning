import timeit

def test1():
    o =[]
    for i in range(1000):
        o = o + [i]
    return o

def test2():
    o =[]
    for i in range(1000):
        o.append(i)
    return o

def test3():
    o = [i for i in range(1000)]
    return o

def test4():
    o = list(range(1000))
    return o


x = list(range(2000000))
y = list(range(2000000))

def adding_list_content():

    t1 = timeit.Timer("test1()", "from __main__ import test1")
    print "concatination", t1.timeit(1000)

    t2 = timeit.Timer("test2()", "from __main__ import test2")
    print "append", t2.timeit(1000)

    t3 = timeit.Timer("test3()", "from __main__ import test3")
    print "list comprehension", t3.timeit(1000)

    t4 = timeit.Timer("test4()", "from __main__ import test4")
    print "list function", t4.timeit(1000)

def pop_validation():
    pop_end = timeit.Timer("x.pop()", "from __main__ import x")
    print "pop end", pop_end.timeit(1000)

    pop_start = timeit.Timer("y.pop(0)", "from __main__ import y")
    print "pop start pos", pop_start.timeit(1000)


# adding_list_content()
pop_validation()
