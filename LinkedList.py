class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        node = Node(value)

        self.head = node
        self.tail = node
        self.length = 1

    def prepend(self, value):
        temp = Node(value)

        temp.next = self.head
        self.head = temp

    def append(self, value):
        temp = Node(value)
        if not self.head:
            self.head = temp
            self.tail = temp
            self.length = 1

        else:
            self.tail.next = temp
            self.tail = temp


    def print_list(self):
        current = self.head

        while current:
            print(current.value)
            current = current.next

    def remove(self, value):
        pass

    def pop(self):
        pass



numbers = LinkedList(34)

numbers.append(5)
numbers.append(12)
numbers.append(73)
numbers.append(98)


numbers.print_list()