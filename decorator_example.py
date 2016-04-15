color = ["red", "blue"]

# simple decorator function
def simple_decorator(funct):
    def inner():
        print "Applying decorator into the function"
        funct()
    return inner

# function decorator with arg
def decorator_with_arg(funct):
    def inner(arg):
        print "Applying decorator into function with arg"
        funct(arg)
    return inner

# function dec with multiple arg
def star(func):
    def inner(*args, **kwargs):
        print "*" * 30
        func(*args, **kwargs)
        print "*" * 30
    return inner

# function dec with multiple arg
def slash(func):
    def inner(*args, **kwargs):
        print "/" * 30
        func(*args, **kwargs)
        print "/" * 30
    return inner

# function dec with passing arg
def decorator_with_passing_arg(args):
    def decorator(fun):
        def inner(*arg, **kwargs):
            if args in color:
                fun(arg)
            else:
                print "sorry select red blue for decorate"
        return inner
    return decorator


# function dec for class
def singleton_decorotor(cls):
    obj = {}

    def instance():
        if cls not in obj:
            obj[cls] = cls()
        return obj[cls]
    return instance

# decorator is class
class class_dec(object):
    def __init__(self, f):
        print "inside init function for class dec"
        self.f = f

    def __call__(self, *args, **kwargs):
        print "inside call function"
        self.f()

class class_dec_with_arg_fun(object):
    def __init__(self, f):
        print "inside the dec funtion"
        self.f = f

    def __call__(self, *args, **kwargs):
        print "calling function"
        self.f(*args, **kwargs)

@simple_decorator
def simple():
    print "original data"

@decorator_with_arg
def with_arg(arg):
    print "orginal data with arg %s", arg


@star
@slash
def chain_decorator(arg):
    print "orginal data of chain dec with arg %s" % arg


@decorator_with_passing_arg("green")
def nested_decorator(arg):
    print "just for nested decorator %s" % arg


@singleton_decorotor
class myclass(object):
    def __init__(self):
        print  "hi this is class "

@class_dec
def dec_class():
    print "function need to be decorated"

@class_dec_with_arg_fun
def dec_class_with_argfun(a, b, c):
    print "this is th parameter list %s %s %s" %(a,b,c)




#############################################################################
#    def outer_decorator(*outer_args,**outer_kwargs):
#     def decorator(fn):
#         def decorated(*args,**kwargs):
#             do_something(*outer_args,**outer_kwargs)
#             return fn(*args,**kwargs)
#         return decorated
#     return decorator
#
# @outer_decorator(1,2,3)
# def foo(a,b,c):
#     print a
#     print b
#     print c
#
#
# foo()
#
# This is equivalent to:
#
# def decorator(fn):
#     def decorated(*args,**kwargs):
#         do_something(1,2,3)
#         return fn(*args,**kwargs)
#     return decorated
# return decorator
#
#
#
# @decorator
# def foo(a,b,c):
#     print a
#     print b
#     print c
#
#
# foo()                                                #
#                                                                           #
                                                                          #
#                                                                           #
#                                                                           #
#                                                                           #
#                                                                           #
#############################################################################


# simple()
# with_arg("Hiiiiiiiiiii")
# chain_decorator("ummmmmmmmmmmmmmmmmmma")

# nested_decorator("hi")

# c = myclass()

j = dec_class()

# obj = dec_class_with_argfun(1,2,3)