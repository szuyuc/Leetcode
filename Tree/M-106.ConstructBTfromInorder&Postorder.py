class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        
        if not len(inorder):
            return None
        
        root = postorder.pop()
        ind = inorder.index(root)
        root_node = TreeNode(root)
    
        root_node.left = self.buildTree(inorder[:ind],postorder[:ind])
        root_node.right = self.buildTree(inorder[ind+1:],postorder[ind:])
        
        return root_node