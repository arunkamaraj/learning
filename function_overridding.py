import time
class parent(object):
    def __init__(self):
        print "This is parent class"

    def log(self,msg):
        print msg, "!!!!"

class child(parent):
    def __init__(self):
        print "This is child"

    def log(self,msg):
        timestamp = time.ctime()
        message = timestamp + "   " + msg
        super(child,self).log(message)


obj = child()
obj.log('hi')
