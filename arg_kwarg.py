# def sum_element(*z):
#     print "z",z
#     return sum(z)
#
#
# def eleminatefirst_add(a,*b):
#     print "b",b
#     s = sum_element(*b)
#     return  s
#
# def kwarg_example(a,b,c):
#     print a,b,c
#
# f = eleminatefirst_add(1,2,3,4)
# print f
#
# d = {"a":1,"c":2,"b":3}
# kwarg_example(**d)


def arg_example(*args, **kwargs):
    print "arg_example"
    print "args", args
    print "kwargs", kwargs
    print "------------------"

def kwarg_example(*args, **kwargs):
    print "kwarg_example"
    print "args", args
    print "kwargs", kwargs
    print "------------------"

def positional_and_arg_example(pos, *args):
    print "positional_and_arg_example"
    print "positional arg", pos
    print "args", args
    print "------------------"

def arg_kwarg_example(*args, **kwargs):
    print "arg_kwarg_example"
    print "args", args
    print "kwargs", kwargs
    print "------------------"

def arg_receive(arg):
    print "arg_receive"
    print arg
    print "------------------"

def kwarg_receive(kwargs):
    print "kwarg_receive", kwargs
    print "__________________"


# arg_example("arun", "kamaraj", "punitha")

# kwarg_example(appa='kamaraj', me='arun', amma='punitha')

# positional_and_arg_example("arun", "kamaraj", "punitha")

# arg_kwarg_example("arun", "kamaraj", "punitha", appa='kamaraj', me='arun', amma='punitha')

arg_data = (1,2,3,4,5)
arg_receive(*arg_data)

# kwarg_data = {"a":1,"c":2,"b":3}
# kwarg_receive(**kwarg_data)







