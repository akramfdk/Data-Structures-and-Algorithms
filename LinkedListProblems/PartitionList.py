"""
List is partitioned in-place such the elements < x are at the beginning of list and >= x at its end

Logic:
- Two dummy nodes dummy_1 and dummy_2 are created
- prev_1 and prev_2 track the last nodes in the sequences pointed to by dummy_1 and dummy_2
- current is used to traverse the original list
- if current element < x, it is added to sequence dummy_1 and prev_1 is moved to this element
- if current element >= x, it is added to sequence dummy_2 and prev_2 is moved to this element
- at the end, prev_1.next is pointed to dummy_2.next and self.head is pointed to dummy_1.next (prev_2.next is set to None)
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value = None):
        self.head = None
        if value:
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

        print("None")

    def partition(self, x):

        if not self.head:
            return
        
        dummy_1 = Node(0)
        prev_1 = dummy_1
        dummy_2 = Node(0)
        prev_2 = dummy_2

        current = self.head
        while current:
            if current.value < x:
                prev_1.next = current
                prev_1 = current
            else:
                prev_2.next = current
                prev_2 = current
            current = current.next

        prev_2.next = None
        prev_1.next = dummy_2.next
        self.head = dummy_1.next


my_list = LinkedList()
my_list.append(3)
my_list.append(9)
my_list.append(6)
my_list.append(15)
my_list.append(1)

my_list.print_list()

my_list.partition(6)
my_list.print_list()