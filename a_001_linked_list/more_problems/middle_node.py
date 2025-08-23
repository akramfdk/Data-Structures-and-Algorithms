# conditions - no length attribute and not allowed to compute length

# maintain two pointers slow and fast
# slow hops one node and fast two nodes
# both start at first node
# when fast reaches end, slow has traversed half the length
# hence slow at middle :)

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
        print("Linked List: ", end="")
        while current:
            print(current.value, end=" -> ")
            current = current.next

        print(None)

    def middle_node(self):
        slow = self.head
        fast = self.head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        return slow

def print_statements(ll):
    ll.print_list()
    middle = ll.middle_node()
    print("Middle Value -> ", end="")
    print(middle.value) if middle else print(None)
    print()

ll = LinkedList()
print_statements(ll)

ll.append(5)
print_statements(ll)

ll.append(3)
print_statements(ll)

ll.append(7)
ll.append(6)
print_statements(ll)

ll.append(9)
ll.append(2)
print_statements(ll)

ll.append(8)
print_statements(ll)
