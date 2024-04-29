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
            print(current.value, end = " ")
            current = current.next

        print()

    def remove(self, value):
        pass

    def pop(self):
        temp = self.head
        cur = self.head

        if not self.head:
            return None
        elif not self.head.next:
            
            self.head = None
            self.tail = None
        else:
            while(cur.next.next):
                cur = cur.next

            temp = cur.next
            self.tail = cur
            self.tail.next = None


        self.length -= 1
        return temp



numbers = LinkedList(34)

numbers.append(5)
numbers.print_list()

print(numbers.pop())
print(numbers.pop())
print(numbers.pop())
