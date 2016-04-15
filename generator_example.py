def gen_1():
    def gen_x():
        yield ("arun")
        yield ("kamaraj")
        yield ("punitha")
        yield ("gandhi")

    x = gen_x()
    for i in range(4):
        print x.next()

def fibonacciexample(data):

    def fib(n):
        a, b, counter = 0, 1, 0
        while True:
            if counter > n: return
            yield a
            a, b = b, a + b
            counter += 1
    x= fib(data)

    for i in x:
        print i



def recursive_generator(data): #tough
    # finding permutation of [a,b,c]
    # algorithms is "a" and remaining list and connection those letter
    l = len(data)
    item = data
    print "before", item
    if l == 0: yield  []
    else:
        for i in range(l):
            print "again recusive for", item[:i] + item[i+1:]
            for j in recursive_generator(item[:i] + item[i+1:]):
                print "final recur", j, "value of Item", item, "item[i]" , item[i]
                yield [item[i]] + j


# generator of generator
def fibonacci():
    """Ein Fibonacci-Zahlen-Generator"""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def numb(n):
    temp = 0
    while temp <= n:
        yield temp
        temp += 1


def firstn(g, n):
    for i in range(n):
        yield g.next()

# print list(firstn(fibonacci(), 10))


# for p in recursive_generator(['r','e','d']):
#     print ''.join(p)

# fibonacciexample (10)

k = numb(10)

g = sum((numb(10)))
print g