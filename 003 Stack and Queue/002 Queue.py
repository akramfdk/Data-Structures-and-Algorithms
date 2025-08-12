# implemenatation of queue using a linked list
# enqueue at tail of linked list O(1)
# dequeue at head O(1)

# we need to add at one end and remove at the other
# python list not suitable as at front O(1) for both add and remove

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self, value=None):
        new_node = Node(value) if value else None
        self.length = 1 if value else 0

        self.first = new_node
        self.last = new_node

    def enqueue(self, value):
        new_node = Node(value)
        if not self.first:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node

        self.length += 1

    def dequeue(self):
        if not self.first:
            return None
        
        temp = self.first
        if not self.first.next:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next
            temp.next = None

        self.length -= 1
        return temp
    
    def print_queue(self):
        temp = self.first

        if not temp:
            print("EMPTY QUEUE")
            return

        while temp.next:
            print(temp.value, end = " <- ")
            temp = temp.next

        print(temp.value)


queue = Queue()
queue.print_queue()

queue.enqueue(3)
queue.enqueue(9)
queue.enqueue(6)

queue.print_queue()

print(queue.dequeue().value)
queue.print_queue()

print(queue.dequeue().value)
queue.print_queue()

print(queue.dequeue().value)
queue.print_queue()

print(queue.dequeue())
queue.print_queue()