class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value=None):
        new_node = None
        self.length = 0
        if value:
            new_node = Node(value)
            self.length = 1
        self.head = new_node
        self.tail = new_node


    def print_list(self):
        temp = self.head
        while temp:
            print(temp.value, end = " -> ")
            temp = temp.next
        print(None)


    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.length += 1
        return True

    def pop(self):
        if not self.head:
            return None
        temp = self.head
        pre = self.head

        while temp.next:
            pre = temp
            temp = temp.next
        
        self.tail = pre
        self.tail.next = None

        self.length -= 1

        if self.length == 0:
            self.head = None
            self.tail = None

        return temp

    def prepend(self, value):
        new_node = Node(value)

        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

        self.length += 1
        return True
    
    def pop_first(self):
        # when we start with no node
        if not self.head:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None

        # when we start with a single node
        if not self.head:
            self.tail = None
        
        self.length -= 1
        return temp
    

ll = LinkedList()

ll.append(5)
ll.print_list()

ll.append(3)
ll.print_list()

ll.pop()
ll.print_list()

ll.pop()
ll.print_list()

ll.pop()
ll.print_list()

ll.prepend(5)
ll.print_list()

ll.prepend(7)
ll.print_list()

ll.prepend(1)
ll.print_list()

ll.pop_first()
ll.print_list()

ll.pop_first()
ll.print_list()

ll.pop_first()
ll.print_list()

ll.pop_first()
ll.print_list()
