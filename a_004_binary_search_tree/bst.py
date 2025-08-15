# A simple implementation of binary search tree insert and contain
# using iterative approach
# recursive approach will be used later in more depth

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None # entry point to the tree

    # logic is that we visit each node and check if value can be inserted
    # to its left or right
    # else we move to the appropriate subtree
    def insert(self, value):
        new_node = Node(value)

        if not self.root:
            self.root = new_node
            return True
        
        temp = self.root
        while True:
            if value == temp.value:
                return False
            elif value < temp.value:
                if not temp.left:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if not temp.right:
                    temp.right = new_node
                    return True
                temp = temp.right

    # go to each node see if the value matches, return True
    # else go left or right
    # if we reach None, value not present, return False
    def contains(self, value):
        temp = self.root

        while temp:
            if value == temp.value:
                return True
            elif value < temp.value:
                temp = temp.left
            else:
                temp = temp.right
        
        return False



    

bst = BinarySearchTree()

bst.insert(10)
bst.insert(5)
bst.insert(15)
bst.insert(12)
bst.insert(8)
bst.insert(3)
bst.insert(18)

print(bst.root.value)
print(bst.root.left.value)
print(bst.root.right.value)
print(bst.root.left.left.value)
print(bst.root.left.right.value)
print(bst.root.right.left.value)
print(bst.root.right.right.value)

print(bst.contains(12))
print(bst.contains(3))
print(bst.contains(9))
print(bst.contains(19))
print(bst.contains(10))