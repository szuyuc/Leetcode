class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        
        """
        Iterative
        """
        if not root:
            return []
        stack = [root]
        arr = []
        while stack: 
            node = stack.pop()
            if node:
                arr.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return arr
               
            
        
        
        
    """
    Recursive 
     if not root:
            return []
        arr = [root.val]
        l = self.preorderTraversal(root.left)
        r = self.preorderTraversal(root.right)
        
        return arr+ l+ r
    
    """   