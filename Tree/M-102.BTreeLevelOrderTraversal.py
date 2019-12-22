class TreeNode:
    def __init__(self,val):
        self.val = val
        self.right = None
        self.left = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        
        if not root:
            return []
        
        stack= [root]
        
        level_arr = []
        
        while stack: 
            temp = []
            store_node = []
            for i in stack:
                if i: 
                    temp.append(i.val)
                    store_node.append(i.left)
                    store_node.append(i.right)

            stack = store_node
            if len(temp) != 0:
                level_arr.append(temp)
        return level_arr
                
                