# partition(self, value)
# partition a linked list such that
# values less than value are at front
# values greater or equal are at the rear
# relative order of the values on either side remains same
# the operation is in-place
# Time complexity is O(n)


# we use two dummy nodes
# one node to take out the nodes with value < value
# other node to take out the nodes with value >= value
# finally we merge these two lists to get the partitioned list
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
        print(None)

    def partition_list(self, value):
        if not self.head:
            return
        
        dummy_1 = Node(-1)
        dummy_2 = Node(-2)

        prev1 = dummy_1
        prev2 = dummy_2

        current = self.head

        while current:
            if current.value < value:
                prev1.next = current
                prev1 = current
            else:
                prev2.next = current
                prev2 = current

            current = current.next

        prev2.next = None
        prev1.next = dummy_2.next
        self.head = dummy_1.next

my_linked_list = LinkedList()
my_linked_list.append(1)
my_linked_list.append(4)
my_linked_list.append(3)
my_linked_list.append(2)
my_linked_list.append(5)
my_linked_list.append(2)
my_linked_list.print_list()
my_linked_list.partition_list(3)
my_linked_list.print_list()