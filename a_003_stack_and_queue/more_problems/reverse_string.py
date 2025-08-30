class Stack:
    def __init__(self):
        self.stack_list = []

    def push(self, value):
        self.stack_list.append(value)

    def pop(self):
        if self.is_empty():
            return None
        return self.stack_list.pop()
    
    def peek(self):
        if self.is_empty():
            return None
        return self.stack_list[-1]

    def is_empty(self):
        return len(self.stack_list) == 0
    
    def size(self):
        return len(self.size)
    

def reverse_string(string):
    my_stack = Stack()
    reversed_string = ""

    for letter in string:
        my_stack.push(letter)
    
    while not my_stack.is_empty():
        reversed_string += my_stack.pop()

    return reversed_string

print(reverse_string("roger that!!"))
