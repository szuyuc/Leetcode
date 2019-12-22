def invertTree(self, root: TreeNode) -> TreeNode:
"""
Recursive
"""        
        if not root:
            return 
        temp = root.left 
        root.left = root.right
        root.right = temp
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        
        return root
        
     
        

"""
Iterative 
""" 
def invertTree(self, root: TreeNode) -> TreeNode:
        head = root
        
        if not root:
            return None
        
        stack = [root]
        while stack:
            node = stack.pop()
            if node.left:
                stack.append(node.left)
            if node.right :
                stack.append(node.right)
            temp = node.left 
            node.left = node.right
            node.right = temp
            
        return head
           
        
            
                    