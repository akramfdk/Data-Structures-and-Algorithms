# for bfs implementation we use a queue
# we visit a node, put its VALUE in results list
# and append its children NODES into a queue
# continue till queue is not empty

from collections import deque

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None


    def insert(self, value):
        new_node = Node(value)

        if not self.root:
            self.root = new_node
            return True

        current = self.root
        while True:
            if value == current.value:
                return False
            elif value < current.value:
                if not current.left:
                    current.left = new_node
                    return True
                current = current.left
            else:
                if not current.right:
                    current.right = new_node
                    return True
                current = current.right

        
    def contains(self, value):
        current = self.root

        while current:
            if value == current.value:
                return True
            elif value < current.value:
                current = current.left
            else:
                current = current.right

        return False


    def bfs(self):
        results = []
        queue = deque()
        queue.append(self.root)

        while queue:
            current = queue.popleft()
            results.append(current.value)

            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

        return results
    

my_tree = BST()

my_tree.insert(50)
my_tree.insert(30)
my_tree.insert(20)
my_tree.insert(40)
my_tree.insert(70)
my_tree.insert(60)
my_tree.insert(80)

print(my_tree.bfs())