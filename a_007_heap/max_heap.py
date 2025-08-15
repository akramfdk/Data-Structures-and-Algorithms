class MaxHeap:
    def __init__(self):
        self.heap = []

    # helper functions
    def _parent(self, index):
        return (index-1)//2
    
    def _left_child(self, index):
        return 2*index+1
    
    def _right_child(self, index):
        return 2*index+2
    
    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def insert(self, value):
        self.heap.append(value)

        current = len(self.heap) - 1

        # bubble up
        while current>0:
            parent = self._parent(current)

            if self.heap[current] > self.heap[parent]:
                self._swap(current, parent)
                current = parent
            else:
                break

    def sink_down(self, index):


        while True:
            left = self._left_child(index)
            right = self._right_child(index)

            max_index = index

            if left < len(self.heap) and self.heap[left] > self.heap[max_index]:
                max_index = left
            
            if right < len(self.heap) and self.heap[right] > self.heap[max_index]:
                max_index = right

            if index == max_index:
                break
            else:
                self._swap(index, max_index)
                index = max_index

    # always remove the max value that is value at index 0
    def remove(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop
        
        temp =self.heap[0]
        self.heap[0] = self.heap.pop()

        self.sink_down(0)

        return temp
    
    def print_heap(self):
        print(self.heap)
    

my_max_heap = MaxHeap()
my_max_heap.insert(90)
my_max_heap.insert(70)
my_max_heap.insert(30)
my_max_heap.insert(60)
my_max_heap.insert(80)
my_max_heap.insert(40)
my_max_heap.insert(50)

my_max_heap.print_heap()

print(my_max_heap.remove())
my_max_heap.print_heap()

print(my_max_heap.remove())
my_max_heap.print_heap()

print(my_max_heap.remove())
my_max_heap.print_heap()
