"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        
        n = []
       
        def travers(root):
            if root:
                n.append(root.val)
                for i in root.children:
                    travers(i)
            
        travers(root)    
        return n
        
    """
    Follow up:iteratively
    """
    
    def preorder(self, root: 'Node') -> List[int]:
        
        if not root:
            return 
        stack = [root]
        n = []
        while stack :
            node = stack.pop()
            n.append(node.val)
            stack.extend(node.children[::-1])
         
        return n      