# queue
# FIFO/LILO
# insert - enqueue
# delete - dequeue
# front, rear
# data

class Queue:

    MAX = 4 # queue can only hold MAX-1 items

    def __init__(self):
        self.data = []
        for i in range(self.MAX):
            self.data.append(0)
        self.front = 0 # location to delete
        self.rear = 0  # location to insert

    def is_empty(self):
        return self.front == self.rear

    def is_full(self):
        return self.size() == self.MAX - 1

    def size(self):
        if self.is_empty():
            return 0
        elif self.front < self.rear:
            return self.rear - self.front
        else: # rear is in front i.e. wrap around
            return self.rear + self.MAX - self.front

    def enqueue(self, value):
        if self.is_full():
            print("Cannot insert to full queue.")
        else: # includes wrap around
            self.data[self.rear] = value
            self.rear = (self.rear + 1) % self.MAX

    def dequeue(self):
        if self.is_empty():
            print("Cannot delete from empty queue.")
            return -1
        else: # includes wrap around
            result = self.data[self.front]
            self.front = (self.front + 1) % self.MAX
            return result

    def peek(self):
        if self.is_empty():
            print("Empty queue.")
        else:
            #return self.data[self.front]
            return self.data[self.front], self.data[self.rear-1]
        
    def display(self):
        if self.is_empty():
            print("Empty queue.")
        else:
            if self.front < self.rear: # no wrap around
                for i in range(self.front, self.rear):
                    print(self.data[i])
            else: # wrap around
                for j in range(self.front, self.MAX):
                    print(self.data[j])
                for k in range(0, self.rear):
                    print(self.data[k])
            
# main
q = Queue()
q.enqueue('a')
q.enqueue('b')
q.enqueue('c')
print(q.dequeue(), "deleted")
q.enqueue('d')
q.display()






                










