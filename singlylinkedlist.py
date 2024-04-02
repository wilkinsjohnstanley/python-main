#Create nodes
#Create Linked List
#Add nodes to linked list
#print linked list

class Node:
    def __init__(self, data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head = None
    def insert(self, newNode):
        #head node is John, points to none
        if self.head = None:
            self.head=newNode
        else:
            self.head.next=newNode

#Node => Data, next points to nothing
firstNode = Node("John")
linkedList = LinkedList()
linkedList.insert(firstNode)
secondNode = Node("Ben")
linkedList.insert(secondNode)
thirdNode = Node("Matthew")
linkedList.insert(thirdNode)
