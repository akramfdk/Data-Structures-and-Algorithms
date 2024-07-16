class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        
        self.length +=1
        return True
    
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
    
    def pop(self):
        if not self.head:
            return None
        else:
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
        
    def pop_first(self):
        if not self.head:
            return None
        else:
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
        else:
            if index < self.length/2:
                temp = self.head
                for _ in range(index):
                    temp = temp.next

                return temp
            else:
                temp = self.tail
                for _ in range(self.length - 1 - index):
                    temp = temp.prev

                return temp
            
    def set(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    def insert(self, index, value):
        new_node = Node(value)
        if index < 0 or index > self.length:
            return False
        elif index == 0:
            return self.prepend(value)
        elif index == self.length:
            return self.append(value)
        else:
            before = self.get(index - 1)
            after = before.next

            before.next = new_node
            after.prev = new_node
            new_node.prev = before
            new_node.next = after

            self.length += 1
            return True
        
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        elif index == 0:
            return self.pop_first()
        elif index == self.length - 1:
            return self.pop()
        else:
            before = self.get(index - 1)
            temp = before.next
            after = temp.next

            before.next = after
            after.prev = before
            temp.prev = None
            temp.next = None

            self.length -= 1
            return temp

    
    def display(self):
        temp = self.head
        while temp:
            print(temp.value, end = " -> ")
            temp = temp.next

        print(None)
    

my_doubly_linked_list = DoublyLinkedList(7)
my_doubly_linked_list.display()

my_doubly_linked_list.append(19)
my_doubly_linked_list.append(4)
my_doubly_linked_list.append(2)
my_doubly_linked_list.append(8)
my_doubly_linked_list.display()

my_doubly_linked_list.prepend(3)
my_doubly_linked_list.display()

my_doubly_linked_list.pop()
my_doubly_linked_list.display()

my_doubly_linked_list.pop_first()
my_doubly_linked_list.display()

print(my_doubly_linked_list.get(0).value)
print(my_doubly_linked_list.get(2).value)
print(my_doubly_linked_list.get(3).value)

my_doubly_linked_list.set(1, 8)
my_doubly_linked_list.display()

my_doubly_linked_list.insert(0, 33)
my_doubly_linked_list.insert(1, 19)
my_doubly_linked_list.insert(6, 41)
my_doubly_linked_list.display()

my_doubly_linked_list.remove(2)
my_doubly_linked_list.remove(0)
my_doubly_linked_list.remove(4)
my_doubly_linked_list.display()
