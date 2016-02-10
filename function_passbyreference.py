def passbyreference(li):
    li.append(100)


def defaultarg(a,b,t,u =100,h =400):
    print a,b,t,u,u,h

def variablelength(a,*b,**c):
    print a
    print b
    print c
# l = [1,2,2,4,5]
# passbyreference(l)
# print l
variablelength(10,[1,2,3],)

# defaultarg(1,2,50,h=500)



