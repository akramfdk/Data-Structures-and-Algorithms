class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def prepend(self, value):
        temp = Node(value)

        temp.next = self.head
        self.head = temp

    def append(self, value):
        temp = Node(value)
        
        if not self.head:
            self.head = temp

        else:
            current = self.head
            while current.next:
                current = current.next
            
            current.next = temp

    def display(self):
        current = self.head

        while current:
            print(current.value, end = " ")
            current = current.next

        print()

    def remove(self, value):
        pass

    def pop(self):
        pass



numbers = LinkedList()

numbers.prepend(11)
numbers.prepend(22)
numbers.append(34)
numbers.append(5)
numbers.append(12)
numbers.prepend(33)
numbers.append(73)
numbers.append(98)


numbers.display()