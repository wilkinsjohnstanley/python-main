# #Use a class approach to manually create methods to intereact with a queue
# class Queue:
#     def __init__(self):
#         self.items=[]
#         self.size=0
#     def empty(self):
#         return self.items ==[]
#     def enqueue(self, data):
#         self.items.insert(0, data)
#         self.size +=1
#     def dequeue(self):
#         data = self.items.pop()
#         self.size -=1
#         return data

#     def size1(self):
#         return self.size

#     def print_q(self):
#         for i in self.items:
#             print(i)

# q = Queue()
# q.enqueue('dog')
# q.enqueue('griffin')
# q.enqueue(69)
# q.print_q()
# print(q.size1())
# q.dequeue()
# q.print_q()
# print(q.size1())

from queue import Queue
q = Queue(maxsize=4)
print(q.qsize())
q.put('bird')
q.put('butterfly')
q.put(150.59)
q.put('catterfly')
print(q)
print('Full? ', q.full())
print(q.get()) #removeReturn
print('Full? ', q.full())
print(list(q.queue)) #print actual list
