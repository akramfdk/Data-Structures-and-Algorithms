class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self, value=None):

        new_node = Node(value) if value else None
        self.head = new_node
        self.tail = new_node
        self.length = 1 if value else 0

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
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if not self.head:
            return None
        temp = self.tail
        if not self.head.next:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None

        self.length -= 1
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        if not self.head:
            return None
        temp = self.head
        if not self.head.next:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None

        self.length -= 1
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        
        temp = self.head
        if index < self.length/2:
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length - 1 - index):
                temp = temp.prev
        
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
        before = self.get(index - 1)

        # set connections
        new_node.prev = before
        new_node.next = before.next
        before.next.prev = new_node
        before.next = new_node

        self.length += 1
        return True


    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        
        curr = self.get(index)

        # set connections
        curr.prev.next = curr.next
        curr.next.prev = curr.prev
        curr.prev = None
        curr.next = None

        self.length -= 1
        return curr

dll = DoublyLinkedList()
dll.print_list()

dll.prepend(2)
dll.print_list()

dll.append(3)
dll.print_list()

print(dll.pop().value)
dll.print_list()

print(dll.pop().value)
dll.print_list()

dll.pop()
dll.print_list()

dll.append(1)
dll.print_list()

dll.prepend(7)
dll.print_list()

print(dll.pop_first().value)
dll.print_list()

print(dll.pop_first().value)
dll.print_list()

dll.pop_first()
dll.print_list()

dll.append(1)
dll.print_list()

dll.prepend(7)
dll.print_list()

dll.prepend(2)
dll.print_list()

print(dll.get(-1))
print(dll.get(0).value)
print(dll.get(1).value)
print(dll.get(2).value)
print(dll.get(3))

print(dll.set_value(-1, 3))
print(dll.set_value(1, 3))
print(dll.set_value(3, 3))

dll.print_list()

print(dll.insert(-1, 9))
print(dll.insert(4, 9))
print(dll.insert(3, 9))
print(dll.insert(0, 5))
print(dll.insert(2, 6))
dll.print_list()

print(dll.remove(-1))
print(dll.remove(6))
print(dll.remove(5).value)
print(dll.remove(0).value)
print(dll.remove(2).value)

dll.print_list()