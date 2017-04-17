# data structures

# array (Python list)
# - fast/direct access A[i]
# - requires contiguous storage
# - expensive to insert/delete
# - static memory allocation

# linked list
# - dynamic memory allocation
# - (more) efficient to insert/delete
# - high(er) cost to search (linear)
# - more flexible/efficient storage

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
        if self.head is None: # if empty linked list
            self.head = n
        else: # non-empty linked list
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

    def search(self, target):
        curr = self.head
        while (curr is not None) and (curr.data != target):
            curr = curr.link
        if curr is not None:
            print("Found!")
        else:
            print("Not found.")

    def delete(self, target=None, position=None):
        if self.head is None: # empty linked list
            print("Cannot delete from empty linked list.")
        else: # non-empty linked list
            if target is not None: # assume distinct values
                prev = self.head
                curr = self.head
                while (curr is not None) and (curr.data != target):
                    prev = curr
                    curr = curr.link
                if curr is not None: # found
                    prev.link = curr.link # delete by bypassing curr
                else:
                    print("Not found.")
            else: # assume position is valid
                prev = self.head
                curr = self.head
                for i in range(position):
                    prev = curr
                    curr = curr.link
                prev.link = curr.link # delete by bypassing curr

    def update(self, old_value, new_value):
        if self.head is None: # empty linked list
            print("Empty linked list")
        else: # non-empty linked list
        curr = self.head
        while (curr is not None) and (curr.data != old_value):
            curr = curr.link
        if curr is not None: # found
            curr.data = new_value
        else:
            print("Not found.")
            
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
ll.display() # show contents after insertion
ll.search(3)
ll.search(5)
ll.delete(3)
ll.display()
ll.delete(5)
ll.update(2,7)
ll.display()
ll.update(5,7)
