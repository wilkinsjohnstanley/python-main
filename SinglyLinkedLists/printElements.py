def printLinkedList(head):
    #create a temporary pointer
    temp = head

    #print until null pointer (None)
    while temp != None:
        print(temp.data)
        #move to next pointer
        temp = temp.next
