class Queue_def():
    def __init__(self):
        self.item = []

    def dequeue(self):
        return self.item.pop()

    def enqueue(self, data):
        self.item.insert(0, data)

    def Isempty(self):
        return self.item == []

    def size(self):
        return len(self.item)


def josephs_problem(obj, data, num):
    for i in data:
        obj.enqueue(i)

    while obj.size() > 1:

        for i in range(num):

            obj.enqueue(obj.dequeue())

        obj.dequeue()

    return obj.item

if __name__ == "__main__":
    escaped = josephs_problem(Queue_def(), [1,2,3,4,5,6,7,8,9,10,77,88,99,44], 100)
    print escaped