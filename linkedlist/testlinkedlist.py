# data structures

# array (Python list)
# - fast/direct access A[i]
# - requires contiguous storage
# - expensive to insert/delete
# - static memory allocation

# linked list
# - dynamic memory allocation

class Node:

    def __init__(self, data=None, link=None):
        self.data = data
        self.link = link


class LinkedList:

    def __init__(self):
        self.head = None

    def size(self):
        total = 0
        curr = self.head
        while curr is not None:
            curr = curr.link
            total += 1
        return total

    def insert(self, data, position=0):
        n = Node(data) # new node n with data value = data and link value = None
        # if empty linked list
        if self.head is None:
            self.head = n
        # non-empty linked list
        else:
            # insert to front
            if position == 0:
                n.link = self.head
                self.head = n
            # insert to rear
            elif position == self.size():
                curr = self.head
                while curr.link is not None:
                    curr = curr.link
                curr.link = n
            # insert in between
            else:
                prev = self.head
                curr = self.head
                for i in range(position):
                    prev = curr
                    curr = curr.link
                n.link = curr
                prev.link = n

    def display(self):
        if self.head is None: # empty linked list
            print("Empty linked list")
        else: # non-empty linked list
            curr = self.head
            while curr is not None:
                print(curr.data)
                curr = curr.link

# main
ll = LinkedList()
ll.insert(1) # insert to empty linked list
ll.insert(2,0) # insert to front
ll.insert(3,ll.size()) # insert to rear
ll.insert(4,1) # insert in between
ll.display()
