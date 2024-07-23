"""
The below code is a simple implementation of a Binary Search Tree that uses iteration to insert or find a value
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class IterativeBST:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        """Iteratively goes through the tree nodes and inserts the node at the correct position"""
        new_node = Node(value)

        if not self.root:
            self.root = new_node
            return True
        
        temp = self.root

        while True:
            if value < temp.value:
                if not temp.left:
                    temp.left = new_node
                    return True
                temp = temp.left
            elif value > temp.value:
                if not temp.right:
                    temp.right = new_node
                    return True
                temp = temp.right
            else:
                return False
            
    def contains(self, value):
        """Iteratively searches the value in the tree, if found returns True, if reaches a dead-end  returns False"""
        temp = self.root

        while temp:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        
        return False
    

nums_tree = IterativeBST()

nums_tree.insert(5)
nums_tree.insert(3)
nums_tree.insert(7)

print(nums_tree.root.value)
print(nums_tree.root.left.value)
print(nums_tree.root.right.value)

print(nums_tree.contains(3))
print(nums_tree.contains(5))
print(nums_tree.contains(7))
print(nums_tree.contains(2))
print(nums_tree.contains(9))