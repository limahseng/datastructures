# Binary search tree

class BST:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, new_data):
        if new_data < self.data: # go left subtree
            if self.left is None: # insert as left leaf node
                self.left = BST(new_data)
            else: # insert to left subtree
                self.left.insert(new_data)
        else: # new_data > self.data, so go right subtree
            if self.right is None: # insert as right leaf node
                self.right = BST(new_data)
            else:
                self.right.insert(new_data)

    def display(self):
        if self.left:
            self.left.display()
        print(self.data, end=' ')
        if self.right:
            self.right.display()
          
# main
bst = BST(50)
bst.insert(30)
bst.insert(70)
bst.insert(10)
bst.insert(40)
bst.insert(60)
bst.insert(90)
bst.display()









