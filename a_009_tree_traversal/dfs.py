class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class rBST:
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
        if not node:
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
            elif not node.right:
                node = node.left
            elif not node.left:
                node = node.right
            else:
                minimum = self.min_value(node.right)
                node.value = minimum
                node.right = self._r_delete(node.right, minimum)
        
        return node

    def r_delete(self, value):
        self._r_delete(self.root, value)

    def pre_order_dfs(self):
        result = []

        def traverse(node):
            if node:
                result.append(node.value)
                traverse(node.left)
                traverse(node.right)

        traverse(self.root)
        return result
    
    def post_order_dfs(self):
        result = []

        def traverse(node):
            if node:
                traverse(node.left)
                traverse(node.right)
                result.append(node.value)
        
        traverse(self.root)
        return result
    
    def in_order_dfs(self):
        result = []

        def traverse(node):
            if node:
                traverse(node.left)
                result.append(node.value)
                traverse(node.right)

        traverse(self.root)
        return result

my_tree = rBST()
my_tree.r_insert(50)
my_tree.r_insert(30)
my_tree.r_insert(40)
my_tree.r_insert(20)
my_tree.r_insert(70)
my_tree.r_insert(60)
my_tree.r_insert(80)

print(my_tree.root.value)
print(my_tree.root.left.value)
print(my_tree.root.right.left.value)

print(my_tree.r_contains(20))
print(my_tree.r_contains(80))
print(my_tree.r_contains(10))

print(my_tree.pre_order_dfs())
print(my_tree.post_order_dfs())
print(my_tree.in_order_dfs())

my_tree.r_delete(50)
print(my_tree.root.value)
print(my_tree.in_order_dfs())
