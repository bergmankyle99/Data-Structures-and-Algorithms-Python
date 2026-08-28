class Node:
    def __init__(self, value):
        self.value = value
        self.neighbours = []

    def __str__(self):
        return f'Node({self.value})'

    def display(self):
        connections = [node.value for node in self.neighbours] # each of the node values for everything in its set of neighbours
        print(f'{self.value} is connected to: {connections}')



ANode = Node('A')
BNode = Node('B')
CNode = Node('C')
DNode = Node('D')
ANode.neighbours.append(BNode)
BNode.neighbours.append(ANode)
CNode.neighbours.append(DNode)
DNode.neighbours.append(CNode)
ANode.display()
BNode.display()
CNode.display()
DNode.display()
