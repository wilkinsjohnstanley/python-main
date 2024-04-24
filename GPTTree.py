class Node:
    def __init__(self, data):
        self.data = data
        self.right_child = None
        self.left_child = None

class Tree:
    def __init__(self):
        self.root_node = None
    
    def insert(self, data):
        node = Node(data)
        if self.root_node is None:
            self.root_node = node
        else:
            current = self.root_node
            while True:
                parent = current
                if node.data < current.data:
                    current = current.left_child
                    if current is None:
                        parent.left_child = node
                        return
                else:
                    current = current.right_child
                    if current is None:
                        parent.right_child = node
                        return

    def search(self, data):
        current = self.root_node
        while current is not None:
            if current.data == data:
                return current
            elif current.data > data:
                current = current.left_child
            else:
                current = current.right_child
        return None

tree = Tree()
tree.insert(5)
tree.insert(2)
tree.insert(7)
tree.insert(1)
tree.insert(9)

for i in range(1, 10):
    found = tree.search(i)
    if found:
        print(f'{i}: Found')
    else:
        print(f'{i}: Not Found')
