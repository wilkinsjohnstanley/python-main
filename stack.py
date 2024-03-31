class Stack:
    def __init__(self):
        self.stack=[]
    def add(self, dataval):
        if dataval not in self.stack:
            self.stack.append(dataval)
            return True
        else:
            return False
    def peek(self):
        return self.stack[-1]
    def remove(self):
        if len(self.stack)<=0:
            return ("No element in the Stack")
        else:
            return self.stack.pop()
AStack = Stack()
AStack.add("An element")
print(AStack.peek())
AStack.add("Another element")
print(AStack.peek())
#Remove
print(AStack.remove())
print(F"Now the top of the stack is: {AStack.peek()}")