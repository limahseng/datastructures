# stack
# LIFO/FILO
# insert - push
# delete - pop
# top
# data

class Stack:

    MAX = 100

    def __init__(self):
        self.data = [] # declare array
        for i in range(self.MAX): # initialise
            self.data.append(0)
        self.top = -1

    def is_empty(self):
        return self.top == -1

    def is_full(self):        
        return self.top == self.MAX - 1
            
    def push(self, new_data):
        if self.is_full():
            print("Cannot insert to full stack.")
        else:
            self.top += 1
            self.data[self.top] = new_data

    def pop(self):
        if self.is_empty():
            print("Cannot delete from empty stack.")
            return -1
        else:
            result = self.data[self.top]
            self.top -= 1
            return result

    def peek(self):
        if self.is_empty():
            print("Empty stack.")
        else:
            return self.data[self.top]

    def display(self):
        if self.is_empty():
            print("Empty stack")
        else:
            for i in range(self.top+1):
                print(self.data[i])
        
# main
##s = Stack()
##s.push('a') # insert
##s.push('b') # insert
##s.push('c') # insert
##s.push('d') # insert (error if MAX = 3)
##s.display()
##print()
##print(s.pop()) # delete
##print(s.pop()) # delete
##print(s.pop()) # delete
##print(s.pop()) # delete
##s.display()

# stack applications
# - recursion
# - convert decimal to binary/octal/hexadecimal
##6 -> 110
##6 // 2 = 3 rem 0
##3 // 2 = 1 rem 1
##1 // 2 = 0 rem 1

base = 16
hexmap = {10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}

s = Stack()
num = 123
while num // base != 0:
    rem = num % base
    s.push(rem)
    num = num // base
rem = num % base
s.push(rem)

while not s.is_empty():
    num = s.pop()
    if num <= 9:
        print(num, end='')
    else:
        print(hexmap[num], end='')












