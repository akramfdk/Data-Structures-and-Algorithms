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
        
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

        self.length += 1

    def append(self, value):
        temp = Node(value)
        if not self.head:
            self.head = temp
            self.tail = temp
            self.length = 1

        else:
            self.tail.next = temp
            self.tail = temp
        
        self.length += 1


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
    
    def get(self, index):
        if index >=0 and index < self.length:
            temp = self.head
            for _ in range(index):
                temp = temp.next
            return temp
        else:
            return None
        
    def set(self, index, value):
        if index >= 0 and index < self.length:
            temp = self.head
            for _ in range(index):
                temp = temp.next
            
            temp.value = value



numbers = LinkedList(34)
numbers.pop()
numbers.prepend(72)
numbers.append(3)
numbers.prepend(11)
numbers.append(5)
numbers.append(69)
numbers.append(14)
numbers.pop()
numbers.print_list()
print(numbers.get(2).value)
numbers.set(2, 101)
print(numbers.get(2).value)
numbers.print_list()
