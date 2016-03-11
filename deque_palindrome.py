class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0,item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

def check_palindrome(obj, data):
    length = len(data)

    for i in data:
        obj.addFront(i)

    # if length % 2 != 0:
    #     while obj.size() > 1:
    #         if obj.removeFront() == obj.removeRear():
    #             return True
    #         else:
    #             return  False
    # else:
    #     while obj.size() > 0:
    #         if obj.removeFront() == obj.removeRear():
    #             return True
    #         else:
    #             return  False
    
    while obj.size() > 1:
        if obj.removeFront() == obj.removeRear():
            return True
        else:
            return  False



if __name__ == "__main__":
    ans = check_palindrome(Deque(), "arra")
    print ans


