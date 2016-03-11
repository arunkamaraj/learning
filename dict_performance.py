import timeit
import random


for i in range(10000, 1000001, 20000):
    # nee to pass the fucion and that respective parameter
    T1 = timeit.Timer("random.randrange(%d) in x" % i, "from __main__ import random,x")
    x = list(range(i))
    list_data = T1.timeit(1000)
    x = {j : None for j in range(i)}
    dict_data = T1.timeit(1000)
    print "try for : ", i, "list_data : ", list_data, "dict_data : ", dict_data