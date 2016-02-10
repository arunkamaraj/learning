rf = open("arun.txt" ,"rb")
data = rf.read()
print "Reading the file :", data
position = rf.tell()
print "Current position : ", position
rf.seek(-10,2)
data = rf.read()
print "Reading after seek the file :" , data
position = rf.tell()
print "Current position after seek : " , position   
# playing with flush
rf.flush()
data = rf.read()
print "Reading the file buffer again after flush :", data
