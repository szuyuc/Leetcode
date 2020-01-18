class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        

        
        def calsum(root, target, cursum):
            
            if not root:
                return False
            
            if not root.left and not root.right:
                return target==cursum+root.val
            
            
            return calsum(root.left,target, cursum+root.val) or calsum(root.right,target, cursum+root.val)
            
        return calsum(root, sum, 0)
        