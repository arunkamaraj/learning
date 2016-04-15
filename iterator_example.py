class yrange:
    def __init__(self, n):
        self.i = 0
        self.n = n
        self.nr = n-1

    def __iter__(self):
        return self

    def next(self):
        if self.i < self.n:
            i = self.i
            self.i += 1
            return i
        else:
            raise StopIteration()

    def next_reverse(self):
        if self.nr > (self.i-1):
            j = self.nr
            self.nr -= 1
            return j
        else:
            raise  StopIteration



d =yrange(3)

# print d.next()
# print d.next()
# print d.next()
# print d.next()

print d.next_reverse()
print d.next_reverse()
print d.next_reverse()
print d.next_reverse()