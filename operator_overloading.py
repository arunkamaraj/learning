class mark(object):

    def __init__(self,subject,score):
        self.subject = subject
        self.score = score

    def __add__(self, other):
        total = self.score + other.score
        return total

    def __lt__(self,other):
        if self.score < other.score:
            return self.score,self.subject
class game(mark):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __add__(self, other):

        return  super(game,self).__add__(other)







# m = mark("maths", 90)
# s = mark("science", 94)
#
# print m + s
# print m < s

obj = game("Temple_run", 100)
obj1 = game("cricket", 90)

print obj + obj1

