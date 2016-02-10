import random

class RandomNumbers:
    def random_choice(self,l):
        # return random.choice(l)
        return random.choice(l)

    def random_randrange(self,start, end, step):
        return random.randrange(start, end, step)

if __name__ == "__main__" :
    seq = [1,2,3,4,(1,2,3,5),["arun","kamaraj"]]
    ran = RandomNumbers()
    print "choice", ran.random_choice(seq)
    print "randrange", ran.random_randrange(100, 1000, 5)
    print "random", random.random()
    print "before shuffle",seq
    random.shuffle(seq)
    print "shuffle", seq
    print "uniform",random.uniform(10,20j)#also accept complex no

