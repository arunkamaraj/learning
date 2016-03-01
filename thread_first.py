import thread
import threading
import time


def timing(name):
    count = 0
    while count < 1:
        time.sleep(1)
        print threading.currentThread().getName(), "Started"
        print "Thread execution time %s" % (time.ctime(time.time()))
        print threading.currentThread().getName(), "Ended"
        count += 1

def with_thread_module():
    try:
        # print "thread st"
        thread.start_new_thread(timing, ("thread1",))
        thread.start_new_thread(timing, ("thread2",))

    except Exception:

        print Exception

    while 1:
        pass


def with_threading_module():
    try:
        T1= threading.Thread(target=timing, args=("thread1",), name="First")# we can give the arguments in this way or inside the function (here)
        T2= threading.Thread(target=timing, args=("thread2",), name="Second")
        T3= threading.Thread(target=timing, args=("thread3",)) # it uses default name

        T1.start()
        T2.start()
        T3.start() # it uses default name
        # thread.start_new_thread(timing, ("thread1",))
        # thread.start_new_thread(timing, ("thread2",))

    except Exception:
        print Exception

    # while 1:
    #     pass


with_threading_module()
# with_thread_module()