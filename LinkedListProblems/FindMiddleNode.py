"""
The code uses two pointers, slow and fast
slow moves forward by one node and fast moves forward by two nodes
This assures slow moves half the length of linked list by the time fast has traversed the entire list
The final position of slow (when fast has reached the end) is the position of middle node
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node

    def append(self, value):
        new_node = Node(value)

        if not self.head:
            self.head = new_node
        else:
            last = self.head
            while last.next:
                last = last.next
            
            last.next = new_node

    def print_linked_list(self):
        temp = self.head

        while temp:
            print(temp.value, end = " -> ")
            temp = temp.next

        print("None")

    def middle_node(self):
        slow = self.head
        fast = self.head

        while fast and fast.next:
            
            slow = slow.next
            fast = fast.next.next

        return slow.value


my_list = LinkedList(5)
my_list.append(9)
my_list.append(1)
my_list.append(7)
# my_list.append(13)

my_list.print_linked_list()

print(my_list.middle_node())