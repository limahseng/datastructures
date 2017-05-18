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

    def search(self, target):
        if self.data == target:
            return "Found"
        elif self.left is None and self.right is None:
            return "Not found"
        elif target < self.data: # go left subtree
            if self.left is None:
                return "Not found"
            else:
                return self.left.search(target)
        else: # target > self.data, go right subtree
            if self.right is None:
                return "Not found"
            else:
                return self.right.search(target)

    def lookup(self, target, parent=None): # returns curr and parent node 
        if self.data == target:
            # return current node and its parent
            return self, parent
        elif target < self.data: # go left
            if self.left is None:
                return None, None
            else:
                return self.left.lookup(target, self)
        else: # target > self.data, go right
            if self.right is None:
                return None, None
            else:
                return self.right.lookup(target, self)            

    def delete(self, target):
        # get node and parent
        node, parent = self.lookup(target)
        if node is not None:
            # case 1: node has 0 child, just delete
            if (node.left is None) and (node.right is None):
                if parent.left is node:
                    parent.left = None
                else:
                    parent.right = None
                del node
            # case 2: node has 1 child, replace node by its child
            elif (node.left is None) != (node.right is None):
                if node.left:
                    n = node.left
                else:
                    n = node.right
                if parent.left is node:
                    parent.left = n
                else:
                    parent.right = n
            # case 3: node has 2 children, replace with inorder successor
            else:
                parent = node
                successor = node.right
                while successor.left:
                    parent = successor
                    successor = successor.left
                # replace node data with successor data
                node.data = successor.data
                # fix successor's parent node child
                if parent.left == successor:
                    parent.left = successor.right
                else:
                    parent.right = successor.right
        else:
            print("Not found")

    def preorder(self): # Root Left Right
        print(self.data, end=' ')        
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()        

    def postorder(self): # Left Right Root
        if self.left:
            self.left.postorder()
        if self.right:
            self.right.postorder()
        print(self.data, end=' ')            

    def inorder(self): # inorder traversal - Left Root Right
        if self.left:
            self.left.inorder()
        print(self.data, end=' ')
        if self.right:
            self.right.inorder()

    def reverse(self): # reverse traversal - Right Root Left
        if self.right:
            self.right.reverse()
        print(self.data, end=' ')
        if self.left:
            self.left.reverse()

    def minimum(self):
        if self.left is None:
            print("Minimum is", self.data)
        else:
            self.left.minimum()

    def maximum(self):        
        if self.right is None:
            print("Maximum is", self.data)
        else:
            self.right.maximum()
            
# main
bst = BST(50)
bst.insert(30)
bst.insert(70)
bst.insert(10)
bst.insert(40)
bst.insert(60)
bst.insert(90)
bst.minimum()
bst.maximum()
print("Inorder: ", end='')
bst.inorder()
print()
print("Preorder: ", end='')
bst.preorder()
print()
print("Postorder: ", end='')
bst.postorder()
print()
print("Reverse: ", end='')
bst.reverse()
print(bst.search(30))
print(bst.search(20))
bst.delete(10) # node with 0 child
bst.display()
print()
bst.delete(30) # node with 1 child
bst.display()
print()
bst.delete(50) # node with 2 children
bst.display()
print()
