import threading
import time

def deamon():
    print "starting", threading.currentThread().getName()
    time.sleep(3)
    print "ending", threading.currentThread().getName()

def nondeamon():
    print "starting", threading.currentThread().getName()
    print "ending", threading.currentThread().getName()

# deamon thread - it wont wait it is independent
d = threading.Thread(target= deamon, name= "deamon")
d.setDaemon(True)

# Non deamon thread - it wait until main thread to close
t = threading.Thread(target= nondeamon, name= "non-deamon")



d.start()
t.start()

t.join(5) # it is very important to syc all threads
d.join(.5) # it blocks completely so we can give time
print "IS ALIVE : ", d.isAlive()

