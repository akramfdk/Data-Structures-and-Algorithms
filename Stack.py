class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def push(self, value):
        new_node = Node(value)

        new_node.next = self.top
        self.top = new_node

        self.height += 1

        return True

    def pop(self):
        if not self.top:
            return None
        
        temp = self.top

        self.top = self.top.next
        temp.next = None

        return temp

    def peek(self):
        if self.top:
            return self.top.value
        return None


    def print_stack(self):
        current_node = self.top

        while current_node:
            print(current_node.value, end = " -> ")
            current_node = current_node.next

        print(current_node)


stack = Stack(3)
stack.push(7)
stack.push(13)
print(stack.peek())
stack.pop()

stack.print_stack()
