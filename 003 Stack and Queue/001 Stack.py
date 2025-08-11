# implementation of stack using linked list
# push and pop at head of linked list O(1)

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self, value=None):
        new_node = Node(value) if value else None
        self.height = 1 if value else 0
        self.top = new_node

    def push(self, value):
        new_node = Node(value)

        new_node.next = self.top
        self.top = new_node

        self.height += 1

    def pop(self):
        if not self.top:
            return None
        
        temp = self.top

        self.top = self.top.next
        temp.next = None
        self.height -= 1

        return temp
    
    def print_stack(self):
        temp = self.top

        while temp:
            print(temp.value, end = " -> ")
            temp = temp.next

        print(None)
        

stack = Stack()

stack.push(5)
stack.push(7)
stack.push(2)

stack.print_stack()

print(stack.pop().value)
stack.print_stack()

print(stack.pop().value)
stack.print_stack()

print(stack.pop().value)
stack.print_stack()

print(stack.pop())
stack.print_stack()