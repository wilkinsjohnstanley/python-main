#Create nodes
#Create linked list
#add nodes to linked list
#print

class Node:
    def __init__(self, data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
    def insert(self,newNode):
        if self.head is None:
            self.head = newNode
        else:
            lastNode = self.head
            while lastNode.next is not None:
                    lastNode=lastNode.next
            lastNode.next = newNode
    def printList(self):
        if self.head is None:
            print("List is empty")
            return
        currentNode = self.head
        while True:
            if currentNode is None:
                break
            print(currentNode.data)
            currentNode=currentNode.next



#Node => data,next
#firstNode.data => John, firstNode.next => None
firstNode = Node("John") #Create an object
#Create a linkedlist to add the node to
linkedList = LinkedList()
linkedList.insert(firstNode)
secondNode = Node("Ben")
linkedList.insert(secondNode)
thirdNode = Node("Matthew")
linkedList.insert(thirdNode)

#see if worked as expected
linkedList.printList()
