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
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head

        for _ in range(index):
            temp = temp.next

        return temp
        

    def set_value(self, index, value):
        temp = self.get(index)

        if temp:
            temp.value = value
            return True
        
        return False

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        pre = self.get(index - 1)

        new_node.next = pre.next
        pre.next = new_node

        self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length-1:
            return self.pop()
        
        pre = self.get(index-1)
        curr = pre.next

        pre.next = curr.next
        curr.next = None

        self.length -= 1
        return curr
    
    def reverse(self):
        before = None
        curr = self.head
        after = self.head

        # first swap the head and tail
        self.head = self.tail
        self.tail = curr

        # now reverse the links
        while curr:
            after = after.next
            curr.next = before
            before = curr
            curr = after

ll = LinkedList()
ll.print_list()

ll.reverse()
ll.print_list()

ll.append(5)
ll.print_list()

ll.reverse()
ll.print_list()

ll.append(3)
ll.append(8)
ll.print_list()

ll.reverse()
ll.print_list()

