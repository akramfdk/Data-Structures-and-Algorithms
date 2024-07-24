class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)

        self.head = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)

        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            
            current.next = new_node

        self.length += 1
    
    def print_list(self):
        current = self.head
        while current:
            print(current.value, end = " -> ")
            current = current.next

        print(current)

    def binary_to_decimal(self):
        result = 0
        current = self.head

        while current:
            result = 2*result + current.value
            current = current.next
        
        return result
    
my_list = LinkedList(1)
my_list.append(0)
my_list.append(1)
my_list.append(0)
my_list.append(1)

my_list.print_list()

print(my_list.binary_to_decimal())