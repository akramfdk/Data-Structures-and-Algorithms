"""
Logic to find kth node from end:
- have two pointers ahead and behind, where "ahead" is ahead :) of "behind" by k nodes.
- now move ahead and behind forward till ahead reaches the end
- the position of behind gives the position of required node
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)

        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            
            current.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.value, end = " -> ")
            current = current.next        
        print("None")

    def kth_node_from_end(self, k):
        if not self.head or k < 1:
            return None
        
        ahead = self.head
        behind = self.head

        for _ in range(k):
            if ahead:
                ahead = ahead.next
            else:
                return None
        
        while ahead:
            ahead = ahead.next
            behind = behind.next

        return behind.value


my_list = LinkedList()
my_list.append(23)
my_list.append(3)
my_list.append(32)
my_list.append(73)
my_list.append(51)
my_list.print_list()

print(my_list.kth_node_from_end(3))
