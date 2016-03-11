class Stack():
    def __init__(self):
        self.item = []

    def push(self, data):
        self.item.append(data)

    def pop(self):
        return self.item.pop()

    def isEmpty(self):
        return self.item == []

    def peek(self):
        return self.item[len(self.item) - 1]  # self.item[-1]

    def size(self):
        return len(self.item)

def parentheses(s, data):
    list_data = list(data)
    for i in range(len(list_data)):
        if list_data[i] in ["(", "{", "["]:
            s.push(list_data[i])
        elif list_data[i] in [")", "}", "]"] and s.isEmpty() == False:
            if isMatch(s.peek(), list_data[i]):
                s.pop()
            else:
                # print "pattern is not matching"
                return False
        elif list_data[i] == ")" and s.isEmpty():
            return False

    if s.isEmpty():
         return True
    else:
        return False

def isMatch(o, c):
    open_data = "([{"
    close_data = ")]}"
    return open_data.index(o) == close_data.index(c)

def decimal_to_binary(obj, data):
    quotient = data
    bin_no = "0b"
    while quotient > 0:
        quotient, remainder = divmod(quotient, 2)
        obj.push(remainder)
    stack = obj.size()
    for i in range(stack):
        temp = obj.pop()
        bin_no = bin_no + str(temp)
    print bin_no

if __name__ == "__main__":
    # print parentheses(Stack(), '((()))')
    # print parentheses(Stack(), '(()')
    # print parentheses(Stack(), '{{([][])}()}')
    # print parentheses(Stack(), '[{()]')
    decimal_to_binary(Stack(), 50)

