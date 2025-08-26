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
            curr = self.head
            while curr.next:
                curr = curr.next

            curr.next = new_node

    def print_list(self):
        curr = self.head

        while curr:
            print(curr.value, end=" -> ")
            curr = curr.next
        
        print(None)

    def remove_duplicates(self):
        if not self.head or not self.head.next:
            return
        
        prev = self.head
        curr = prev.next

        value_set = set()
        value_set.add(prev.value)

        while curr:
            if curr.value in value_set:
                prev.next = curr.next
                curr.next = None
                curr = prev.next
            else:
                value_set.add(curr.value)
                prev = prev.next
                curr = curr.next

ll = LinkedList()
ll.append(5)
ll.append(5)
ll.append(5)
ll.append(3)
ll.append(3)
ll.append(5)
ll.append(4)
ll.append(2)
ll.append(3)
ll.append(1)
ll.append(1)
ll.append(1)
ll.print_list()

ll.remove_duplicates()
ll.print_list()

