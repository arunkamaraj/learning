import threading
import time


def summa():
    print "yeahhhhhhhhhhhh it is working"


def thread_timer():
    t1 = threading.Timer(3, summa)
    t1.setName("T1")
    t2 = threading.Timer(3, summa)
    t2.setName("T2")

    t1.start()
    t2.start()

    print "waiting befor canceling", t1.getName()
    print "canceled", t1.cancel()


def blocked(obj):
    print "started", threading.currentThread().getName()
    obj.wait()

    print "Hi this is blocked thread", time.ctime(time.time())

def temp_block(obj):
    print "started", threading.currentThread().getName()
    obj.wait(6)
    print "Hi this is temp blocked thread", time.ctime(time.time())
    # if e.isSet():
    #     print "Hi this is temp blocked thread", time.ctime(time.time())
    # else:
    #     print "doing other task"


def blocked_with(obj):
    print "started", threading.currentThread().getName()
    with obj:
        obj.wait()
        print "Hi this is blocked thread", time.ctime(time.time())

def temp_block_with(obj):
    print "started", threading.currentThread().getName()
    with obj:
        obj.wait(6)
        print "Hi this is temp blocked thread", time.ctime(time.time())
        print "calling notify"
        obj.notifyAll()


def thread_event(): # no need to acquire lock
    e = threading.Event()

    T1 = threading.Thread(target=blocked, args=(e,))
    T1.setName("Blocked thread")

    T2 = threading.Thread(target=temp_block, args=(e,))
    T2.setName("Temp block thread")

    T1.start()
    T2.start()

    # print "sleeping 3 sec", time.ctime(time.time())
    time.sleep(10)
    e.set()


def thread_condition(): # need to a

    cond = threading.Condition()

    T1 = threading.Thread(target=blocked_with, args=(cond,))
    T1.setName("Blocked thread")

    T2 = threading.Thread(target=temp_block_with, args=(cond,))
    T2.setName("Temp block thread")

    T1.start()
    T2.start()

    # print "sleeping 3 sec", time.ctime(time.time())
    # cond.notifyAll()


# thread_event()
thread_condition()
