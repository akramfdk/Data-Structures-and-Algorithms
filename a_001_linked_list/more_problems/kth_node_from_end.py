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
        print("Linked List: ", end="")
        current = self.head

        while current:
            print(current.value, end = " -> ")
            current = current.next

        print(None)

    def kth_node_from_end(self, end_index):
        behind = self.head
        ahead = self.head

        for _ in range(end_index):
            if ahead:
                ahead = ahead.next
            else:
                return None
        
        while ahead:
            ahead = ahead.next
            behind = behind.next

        return behind

ll = LinkedList()

ll.append(10)
ll.append(5)
ll.append(2)
ll.append(7)
ll.append(1)
ll.append(9)

ll.print_list()

print(ll.kth_node_from_end(1).value)
print(ll.kth_node_from_end(2).value)
print(ll.kth_node_from_end(3).value)
print(ll.kth_node_from_end(4).value)
print(ll.kth_node_from_end(5).value)
print(ll.kth_node_from_end(6).value)
print(ll.kth_node_from_end(7))