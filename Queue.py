class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.front = new_node
        self.back = new_node
        self.length = 1

    def enqueue(self, value):
        # node added at the back (O(1))
        new_node = Node(value)
        if not self.front:
            self.front = new_node
            self.back = new_node
        else:
            self.back.next = new_node
            self.back = new_node
        
        self.length += 1

    def dequeue(self):
        # node removed from front (O(1))
        if not self.front:
            return None
        temp = self.front
        if not self.front.next:
            self.front = None
            self.back = None
        else:
            self.front = self.front.next
            temp.next = None

        self.length -= 1
        return temp
    
    def print_queue(self):
        if not self.front:
            print("Empty")
            return
        
        temp = self.front

        while temp.next:
            print(temp.value, end = " <- ")
            temp = temp.next

        print(temp.value)

nums_queue = Queue(5)
nums_queue.print_queue()

nums_queue.enqueue(7)
nums_queue.print_queue()

nums_queue.enqueue(2)
nums_queue.enqueue(11)
nums_queue.enqueue(8)
nums_queue.print_queue()

nums_queue.dequeue()

nums_queue.print_queue()

nums_queue.dequeue()
nums_queue.dequeue()
nums_queue.dequeue()
nums_queue.dequeue()
nums_queue.dequeue()

nums_queue.print_queue()