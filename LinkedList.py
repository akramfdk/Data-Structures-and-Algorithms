class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:

    # initialize the linked list (head, tail and length)
    def __init__(self, value):
        node = Node(value)

        self.head = node
        self.tail = node
        self.length = 1


    # add a node to the beginning of the linked list
    def prepend(self, value):
        
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

        self.length += 1


    # add a node at the end of the linked list
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


    # insert the node at a given index of the linked list
    def insert(self, index, value):
        new_node = Node(value)

        if index == 0:
            self.prepend(value)
        elif index == self.length:
            self.append(value)
        elif index > 0 and index < self.length:
            temp = self.get(index - 1)
            new_node.next = temp.next
            temp.next = new_node
            self.length += 1
        else:
            return False
        
        return True


    # print the elements of the linked list in a single line separated by space
    def print_list(self):
        current = self.head

        while current:
            print(current.value, end = " ")
            current = current.next

        print()


    # remove and return the last node from the linked list
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


    # remove and return the first node from the linked list
    def pop_first(self):
        if self.length == 0:
            return None
        
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length = self.length - 1
        
        if self.length == 0:
            self.tail = None

        return temp


    # remove and return the node at a given index from the linked list
    def remove(self, index):
        if index == 0:
            return self.pop_first()
        elif index == self.length - 1:
            return self.pop()
        elif index > 0 and index < self.length - 1:
            prev = self.get(index - 1)
            node_to_remove = prev.next

            prev.next = node_to_remove.next
            node_to_remove.next = None

            self.length -= 1

            return node_to_remove
        else:
            return None


    # return the node at a given index in the linked list
    def get(self, index):
        if index >=0 and index < self.length:
            temp = self.head
            for _ in range(index):
                temp = temp.next
            return temp
        else:
            return None


    # set the value at a given index in the linked list
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    

    # reverse the linked list
    def reverse(self):

        if self.length >= 2:
            temp = self.head
            self.head = self.tail
            self.tail = temp

            cur = self.tail
            nex = cur.next

            while nex.next:
                temp = cur
                cur = nex
                nex = nex.next

                cur.next = temp

            nex.next = cur
            self.tail.next = None







numbers = LinkedList(34)
numbers.pop()
numbers.prepend(72)
numbers.append(3)
numbers.prepend(11)
numbers.append(5)
numbers.append(69)
numbers.append(14)
numbers.pop()
numbers.insert(0, 7)
numbers.insert(3, 77)
numbers.insert(numbers.length, 777)
numbers.print_list()
numbers.pop_first()
numbers.set_value(2, 101)
numbers.print_list()
numbers.remove(0)
numbers.remove(2)
numbers.remove(numbers.length - 1)
numbers.print_list()

numbers.reverse()
numbers.print_list()
