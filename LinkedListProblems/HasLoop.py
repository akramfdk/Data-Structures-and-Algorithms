"""
The logic to detect a loop in linked list:
- start slow and fast pointers, slow moves ahead one node at a time and fast moves ahead two nodes each time
- if there is a cycle in linked list, both slow and fast will be stuck in it, fast will chase slow one node 
    at a time and finally catch up
- if there is no cycle, the fast pointer will reach the end
"""
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        new_node = Node(value)

        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def print_list(self):
        current = self.head

        while current:
            print(current.value, end = " -> ")
            current = current.next

        print("None")

    def create_loop(self):
        if self.head and self.head.next:
            current = self.head
            while current.next is not self.tail:
                current = current.next

            self.tail.next = current
            return True            
            
        return False

    def has_loop(self):
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if fast is slow:
                return True

        return False


my_list_1 = LinkedList()
my_list_1.append(3)
my_list_1.append(13)
my_list_1.append(19)
my_list_1.create_loop()

print("my_list_1 has Loop:", my_list_1.has_loop())
if not my_list_1.has_loop():
    my_list_1.print_list()

my_list_2 = LinkedList()
my_list_2.append(3)
my_list_2.append(13)
my_list_2.append(19)

print("my_list_2 has Loop:", my_list_2.has_loop())

if not my_list_2.has_loop():
    my_list_2.print_list()