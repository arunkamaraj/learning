import threading
import time

class MyThread(threading.Thread):

    def __init__(self, t_id, name):
        super(MyThread, self).__init__()
        self.ID = t_id
        self.Name = name

    def run(self):
        lock.acquire()
        print "Thread %s started" %(self.ID)
        self.timing()
        print "Thread %s ended" %(self.ID)
        lock.release()

    def timing(self):
        count = 0
        while count < 5:
            print "%s Name is %s" %(self.ID, self.Name)
            count += 1



lock = threading.Lock()

T1 = MyThread("001", "THREAD 1")
T2 = MyThread("002", "THREAD 2")

T1.start()
T2.start()
