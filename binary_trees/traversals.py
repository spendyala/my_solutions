

class Node(object):
    '''Binary Tree Node'''
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree(object):
    '''Building binary Tree'''
    def __init__(self, data):
        self.root = Node(data)

    def addLeft(self, data):
        if self.root.left is None:
            self.root.left = Node(data)
        else:
            binary_tree_obj = Node(data)
            binary_tree_obj.left = self.root.left
            self.root.left = binary_tree_obj

    def addRight(self, data):
        if self.root.right is None:
            self.root.right = Node(data)
        else:
            binary_tree_obj = Node(data)
            binary_tree_obj.right = self.root.right
            self.root.right = binary_tree_obj

    def getRightChild(self):
        return self.root.right

    def getLeftChild(self):
        return self.root.left

    def setRightChild(self, value):
        self.root.right = value

    def setLeftChild(self, value):
        self.root.left = value

    def setRootValue(self, value):
        self.root.data = value

    def getRootValue(self):
        return self.root.data

    def __repr__(self):
        return str(self.root.data)


binary_tree = BinaryTree(10)
binary_tree.addLeft(20)
binary_tree.addLeft(34)
binary_tree.addRight(4)
binary_tree.addRight(50)

print(binary_tree)  # This prints only the node


# Create Binary tree
