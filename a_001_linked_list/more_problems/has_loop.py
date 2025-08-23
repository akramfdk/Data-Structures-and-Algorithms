# if there is no loop, fast reaches the end and slow and fast are never equal
# if there is a loop, fast and slow both will enter the loop
# fast will always approach slow one hop at a time and meet it at some point
# hence if slow and fast meet, it means there is a loop
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node


    def has_loop(self):
        slow = self.head
        fast = self.head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if slow is fast:
                return True
            
        return False
    
    def print_list(self):
        if not self.has_loop():
            current = self.head
            print("Linked List: ", end="")
            while current:
                print(current.value, end=" -> ")
                current = current.next
            print(None)
        else:
            print("Linked List has a loop!!!")


ll = LinkedList()
ll.append(2)
ll.append(7)
ll.append(5)
ll.append(1)
ll.append(3)

print("Loop:",ll.has_loop())
ll.print_list()

print()

ll.tail.next = ll.head.next.next # introducing a loop
print("Loop:",ll.has_loop())
ll.print_list()
