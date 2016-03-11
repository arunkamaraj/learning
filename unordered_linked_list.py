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


class Unordered_likedlist():
    def __init__(self):
        self.head = None

    def add_node(self, data):
        temp = Node(data)
        temp.Next = self.head
        self.head = temp

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
        prevoius_node = None
        found = False
        while current_node is not None and found is False:
            if current_node.get_data() == data:
             prevoius_node.set_next(current_node.get_next())
             found = True

            else:
                prevoius_node = current_node
                current_node = current_node.get_next()

        return found


ll = Unordered_likedlist()

ll.add_node(31)
ll.add_node(77)
ll.add_node(17)
ll.add_node(93)
ll.add_node(26)
ll.add_node(54)

output = ll.remove_node(25)
# ans = ll.search_node(26)
# print ans
print output

