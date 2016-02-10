import time

def getsleep():
    time.sleep(2.5)

# clock takes processor time
t0 = time.clock()
getsleep()
print time.clock() - t0 , "processing time"

# time takes wall time
t0 = time.time()
getsleep()
print time.time() - t0 ,"overall time"



print __name__