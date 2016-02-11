""" important is if we are running from __main__ then when exit the program it clear the all object ..
but in shell or in cammand line it wont call the __del__ we need to call manually
"""

class Example:
    def __init__(self, x):
        self.x = x

    def __del__(self):
        print "destructor to clear the object"

    def calculate(self):
        self.x += 10

class ExceptionExample():
    def __init__(self, y):
        self.y = y
        self.y.strip()

    def __del__(self):
        print "Exception in constructor"

# >>> import constructor_destructor as c
# >>> o = c.Example(10)
# >>> del o
# destructor to clear the object


if __name__ == "__main__":
    obj = Example(10)
    del obj
    try:
        ex = ExceptionExample(10)
    except Exception:
        print "Exception",Exception

# """
# >>> import sys
# >>> import gc
# >>> import types
# >>>
# >>> for obj in gc.get_objects():
# ...   if isinstance(obj, MyClass):
# ...     for i in gc.get_referrers(obj):
# ...       if isinstance(i, types.FrameType):
# ...         print repr(i)
# ...
# <frame object at 0x1af19c0>
# >>> sys.last_traceback.tb_next.tb_frame
# <frame object at 0x1af19c0>
# """



