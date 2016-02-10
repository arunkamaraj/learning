#sort of the databased on the age

data = [('arun','m',25),('kamaraj','m',50),('kutti','f',3)]
data_age = sorted(data,key = lambda x : x[2])

print "before arragement ", data
print "after arragement", data_age

