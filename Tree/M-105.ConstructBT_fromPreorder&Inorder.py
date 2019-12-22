class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:

        
        def split(pre_arr, in_arr):
            root_val = pre_arr[0]
            split_ind = -1
            for ind,val in enumerate(inorder):
                if root_val == val: 
                    split_ind = ind 
            if split_ind == -1:
                return None
            
            return split_ind
            
        
        
        if len(preorder)!=len(inorder) or len(preorder) == 0 :
            return None

        if len(preorder) == 1:
            return TreeNode(preorder[0])

        root = TreeNode(preorder[0])
        # we can use inorder.index(preorder[0])
        split_p = split(preorder, inorder)
        
        root.left = self.buildTree(preorder[1:split_p+1],inorder[:split_p])
        if split_p+1<len(inorder):
            root.right = self.buildTree(preorder[split_p+1:],inorder[split_p+1:])
    
        return root
