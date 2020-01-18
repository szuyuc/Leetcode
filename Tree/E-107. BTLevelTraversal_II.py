class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        
        
        if not root:
            return None
        
        stack = [root]
        rtn = []
        while stack:
            rtn.append([node.val for node in stack])
            temp = []
            for node in stack:
                if node.left: temp.append(node.left)
                if node.right:temp.append(node.right)
            if len(temp)!=0:
                stack = temp
            else:
                return reversed(rtn)