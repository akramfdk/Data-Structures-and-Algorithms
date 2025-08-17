class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class r_bst:
    def __init__(self):
        self.root = None

    def _r_insert(self, node, value):
        if not node:
            return Node(value)
        if value < node.value:
            node.left = self._r_insert(node.left, value)
        elif value > node.value:
            node.right = self._r_insert(node.right, value)

        return node

    def r_insert(self, value):
        self.root = self._r_insert(self.root, value)

    
    def _r_contains(self, node, value):
        if not node: # when we reach a leaf node
            return False
        if value == node.value:
            return True
        elif value < node.value:
            return self._r_contains(node.left, value)
        else:
            return self._r_contains(node.right, value)

    def r_contains(self, value):
        return self._r_contains(self.root, value)
    

    def min_value(self, node):
        while node.left:
            node = node.left

        return node.value
    
    def _r_delete(self, node, value):
        if not node:
            return None
        if value < node.value:
            node.left = self._r_delete(node.left, value)
        elif value > node.value:
            node.right = self._r_delete(node.right, value)
        else:
            if not node.left and not node.right:
                return None
            elif not node.left:
                node = node.right
            elif not node.right:
                node = node.left
            else:
                min_val = self.min_value(node.right)
                node.value = min_val
                node.right = self._r_delete(node.right, min_val)
            
        return node

    def r_delete(self, value):
        self._r_delete(self.root, value)
    


my_tree = r_bst()

my_tree.r_insert(50)
my_tree.r_insert(30)
my_tree.r_insert(70)
my_tree.r_insert(20)
my_tree.r_insert(40)
my_tree.r_insert(60)
my_tree.r_insert(80)

print(my_tree.root.value)
print(my_tree.root.left.value)
print(my_tree.root.right.value)
print(my_tree.root.left.left.value)
print(my_tree.root.left.right.value)
print(my_tree.root.right.left.value)
print(my_tree.root.right.right.value)

print(my_tree.r_contains(40))
print(my_tree.r_contains(10))
print(my_tree.r_contains(90))
print(my_tree.r_contains(60))
print(my_tree.r_contains(20))

my_tree.r_delete(40)
print(my_tree.root.left.right)

my_tree.r_delete(30)
print(my_tree.root.left.value)

my_tree.r_delete(50)
print(my_tree.root.value)
print(my_tree.root.right.left)