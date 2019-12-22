"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
"""
Follow up:

Recursive solution is trivial, could you do it iteratively?
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        
        if not root:
            return []
        
        stack = [root]
        n = []

        while stack :
            node = stack.pop()
            if not node.children:
                n.append(node.val)
            else:
                stack.append(Node(node.val,None))
                stack.extend(node.children[::-1])
            
        return n
                    