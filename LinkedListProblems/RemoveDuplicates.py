"""
Remove the duplicates from the linked list
Logic:
- initiate a set and traverse the list using two pointers, prev and current (current is just ahead of prev)
- if the value of current node is in the set, remove that node, else add it to the set (both are O(1) operations)
- continue till current is None 
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
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.value, end = " -> ")
            current = current.next

        print(current)

    def remove_duplicates(self):
        if not self.head or not self.head.next:
            return
        prev = self.head
        curr = prev.next

        values = set()

        while curr:
            if curr.value in values:
                prev.next = curr.next
                curr = prev.next
            else:
                values.add(curr.value)
                prev = prev.next
                curr = curr.next



my_list = LinkedList(3)
my_list.append(15)
my_list.append(9)
my_list.append(8)
my_list.append(2)
my_list.append(3)
my_list.append(15)
my_list.append(19)
my_list.append(23)
my_list.append(2)
my_list.append(2)
my_list.append(2)

my_list.print_list()
my_list.remove_duplicates()
my_list.print_list()