def sum_element(*z):
    print "z",z
    return sum(z)


def eleminatefirst_add(a,*b):
    print "b",b
    s = sum_element(*b)
    return  s

def kwarg_example(a,b,c):
    print a,b,c

# f = eleminatefirst_add(1,2,3,4)
# print f
d = {"a":1,"c":2,"b":3}
kwarg_example(**d)