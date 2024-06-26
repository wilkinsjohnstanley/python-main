#create a class to define a node
class Node:
    def __init__(self, data):
        self.data=data
        self.right_child=None
        self.left_child=None
#Binary Search Tree
class Tree:
    def __init__(self):
        self.root_node=None
    def insert(self, data):
        node = Node(data)
        if self.root_node is None:
            self.root_node = node
        else:
            current = self.root_node
            parent = None
            while True:
                parent = current
                if node.data < parent.data:
                    current = current.left_child
                    if current is None:
                        parent.left_child=node
                        return
                    else:
                        current = current.right_child
                        if current is None:
                            parent.right_child=node
                            return
    def search(self, data):
        current = self.root_node
        while True:
            if current is None:
                return None
                #identity, not equality
            elif current.data is data:
                return data
            elif current.data > data:
                current = current.left_child
            else:
                current = current.right_child


'''
simple implementation:
first assign nodes to be the 1st node and then the child nodes
'''
n1 = Node('root node')
n2 = Node('left child node')
n3 = Node('right child node')
n4 = Node('left grandchild node')

n1.left_child=n2
n1.right_child=n3
n2.left_child=n4
'''place yourself at root'''
current = n1
while current:
    print(current.data)
    current = current.right_child
tree = Tree()
tree.insert(5)
tree.insert(2)
tree.insert(7)
tree.insert(1)
tree.insert(9)

for i in range(1, 10):
    found = tree.search(i)
    print(f'{i}: {found}')