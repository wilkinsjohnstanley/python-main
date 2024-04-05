# class Stack:
#     def __init__(self):
#         self.stack=[]
#     def empty(self):
#         return (len(self.stack))==0
#     def push(self, item):
#         self.stack.append(item)
#         print('Pushed to stack: ', item)
#         print('stack: ', self.stack)

#     #remove method Pop!
#     def pop_stack(self):
#         print(self.stack.pop())
#         print(self.stack)
# s = Stack()
# s.push('ah')
# s.push('buh')
# s.push('cuh')
# s.pop_stack()

from queue import LifoQueue
stack2=LifoQueue()
stack2.put('uh')
stack2.put('buh')
stack2.put('cuh')

print('Stack 2: ', stack2)
print(list(stack2.queue))