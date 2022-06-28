#User function Template for python3

'''
@input - 
node - root node of given tree
k = distance of nodes required 

class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''

#Function to return count of nodes at a given distance from leaf nodes.
def printKDistantfromLeaf(root, k):
    #code here
    leaf_node = list()
    children = dict()
    ptr = root

    def visitor(node):
        if not node.left and not node.right:
            leaf_node.append(node)
            return
        else:
            if node.left: visitor(node.left)
            if node.right: visitor(node.right)
    print(leaf_node)

class Node:
    def __init__(self,val):
        self.right = None
        self.data = val
        self.left = None

_1 = Node(1)
_2 = Node(2)
_3 = Node(3)
_4 = Node(4)

_1.left = _2
_1.right = _4
_2.left = _3

printKDistantfromLeaf(_1)