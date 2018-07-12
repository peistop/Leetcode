class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def createTreeNode(arr):
    nodes = [TreeNode(val) if val else None for val in arr]
    children = nodes[::-1]
    root = children.pop()
    for node in nodes:
        if node:
            if children:
                node.left = children.pop()
            if children:
                node.right = children.pop()
    return root
        
        
    
