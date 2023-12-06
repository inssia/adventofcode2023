class Node():
    def __init__(self, val):
        self.val = val
        self.next = None

node_A = Node('A')
node_B = Node('B')
node_C = Node('C')

node_A.next = node_B
node_B.next = node_C

def recursivePrint(head):
    if head == None:
        return []
    
    return [head.val] + recursivePrint(head.next) 

print(recursivePrint(node_A))

