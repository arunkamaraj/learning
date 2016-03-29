def binarytree(root):
    return [root, [], []]

def getLeft(tree):
    return tree[1]

def getRight(tree):
    return tree[2]

def getRoot(tree):
    return tree[0]


def setRoot(tree, root):
    tree[0] =  root

def setLeft(tree, left):
    l = tree[1]
    if len(l) > 1:

        tree[1]= [left, l, []]

    else:
        tree[1]= [left, [], []]

def setRight(tree, right):
    r = tree[2]
    if len(r) > 1:
        tree[2]= [right, [], r]

    else:
        tree[2]= [right, [], []]


# r = binarytree(3)
# setLeft(r,4)
# setLeft(r,5)
# setRight(r,6)
# setRight(r,7)
# l = getLeft(r)
# print(l)
#
# setRoot(l,9)
# print(r)
# setLeft(l,11)
# print(r)
# print(getRight(getRight(r)))