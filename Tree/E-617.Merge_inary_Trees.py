"""
    DFS
"""
def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
    
    if not t1 and not t2: 
        return None
    
    if not t1:
        return t2
    if not t2:
        return t1
    
    t1.val = t1.val+t2.val
    t1.right = self.mergeTrees(t1.right,t2.right)
    t1.left = self.mergeTrees(t1.left,t2.left)
    
    return t1


"""
    BFS
"""

def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        
        if not t1 and not t2 :
            return None
        
        if not t1:
            return t2
        if not t2:
            return t1
        
        stack = [(t1,t2)]
        while stack:
            n1,n2 =stack.pop()
            n1.val = n1.val+n2.val
            
            if n1.left  and n2.left :
                stack.append((n1.left,n2.left))
            
            if n1.right and n2.right:
                stack.append((n1.right,n2.right))
        
            
            if not n1.left:
                n1.left = n2.left
            if not n1.right :
                n1.right = n2.right
            
            
        return t1
        
        
        
        
       