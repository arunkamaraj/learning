class binarytree():
    def __init__(self, root):
        self.root = root
        self.left = None
        self.right = None

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right

    def getRoot(self):
        return self.root


    def setRoot(self, root):
        self.root = root

    def setLeft(self, left):
        if self.left == None:
            self.left = binarytree(left)
        else:
            t = binarytree(left)
            t.left = self.left
            self.left = t


    def setRight(self, right):
        if self.right ==None:
            self.right = binarytree(right)
        else:
            t = binarytree(right)
            t.right = self.right
            self.right = t


