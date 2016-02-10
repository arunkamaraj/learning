w = open("Filenext", "wb")
w.write("this is one \nthis is two \nthis is three \nthis is four \n")

w.close()
r = open("Filenext", "rb")

def nextexample():
    global r
    for i in range(3):
        nextdata = r.next()
        # r.read() # it wot allow the read bcz it ll mix with iterator
        # r.readlines() # it wot allow the readlines also bcz it ll mix with iterator
        print nextdata

    r.close()

def readlineexample():
    global r
    for i in range(3):
        data = r.readline()
        print data
    r.close()

def readlinesexample():
    global r
    data = r.readlines(0)
    print data
    r.close()


# readlineexample()
# nextexample()
readlinesexample()

