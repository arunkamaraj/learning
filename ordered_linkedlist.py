class Node():
    def __init__(self, data):
        self.Data = data
        self.Next = None

    def get_data(self):
        return self.Data

    def get_next(self):
        return self.Next

    def set_data(self, data):
        self.Data = data

    def set_next(self, next_ref):
        self.Next = next_ref


class Ordered_likedlist():
    def __init__(self):
        self.head = None

    def add_node(self, data):
        temp = Node(data)
        current_node = self.head
        previous_node = None
        stop = False

        # if current_node is not None and current_node.get_next() is not None:
        while current_node is not None and not stop:

            if current_node.get_data() > data:
                  stop = True

            else:
                previous_node = current_node
                current_node = current_node.get_next()

        if previous_node == None:
            temp.set_next(self.head)
            self.head = temp
        else:
            temp.set_next(current_node)
            previous_node.set_next(temp)


    def search_node(self, data):
        current_node = self.head
        found = False
        while current_node is not None and found is False:
            if current_node.get_data() == data:
                found = True
            else:
                current_node = current_node.get_next()

        return found

    def remove_node(self, data ):
        current_node = self.head
        prevoius_node = self.head
        found = False
        while current_node is not None and found is False:
            if current_node.get_data() == data:
             prevoius_node.set_next(current_node.get_next())
             found = True

            else:
                prevoius_node = current_node
                current_node = current_node.get_next()

        return found

    def append_node(self, item):
        current_node = self.head

        while (current_node is not None) and (current_node.get_next() is not None):
            current_node = current_node.get_next()
        else:
            temp = Node(item)

        if current_node is None:
            temp.set_next(current_node)
            self.head = temp
        else:
            temp.set_next(current_node.get_next())
            current_node.Next = temp


l = Ordered_likedlist()

l.add_node(31)
# l.add_node(77)
l.add_node(17)
# l.add_node(93)
# l.add_node(26)
# l.add_node(54)

# s1 = l.search_node(31)
# s2 = l.search_node(17)
#
# print s1, s2


current = l.head
print current

while current.get_next() != None:
    info =  current.get_data()
    print info
    current = current.get_next()

# ans_1= ll.search_node(26)
# output = ll.remove_node(26)
# ans_2 = ll.search_node(26)
# print "first search for 26 ", ans_1, "\n", "removing result is ", output, "\n", "search after removal", ans_2
#
# ll.append_node(26)
# ans_3 = ll.search_node(26)
# print "search after append", ans_3


