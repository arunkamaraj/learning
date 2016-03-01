import threading
import time

class MyThread(threading.Thread):
    def __init__(self, t_id, name ):
        super(MyThread, self).__init__()
        self.ID = t_id
        self.Name = name

    @staticmethod
    def print_now():
        print time.ctime(time.time())

    def run(self):
        print "Started Thread %d" %(self.ID)
        self.timing(self.ID, self.Name)
        # self.print_now()
        print "Finished Thread %d" %(self.ID)

    def timing(self, thread_id, name):
        count = 0
        while count < 5:
            time.sleep(.5)
            print "Thread name and ID is %s %d and time %s\n" %(name, thread_id, time.ctime(time.time()))
            count += 1

T1 = MyThread(1, "THREAD1" )
T2 = MyThread(2, "THREAD2")

T1.start()
T2.start()
