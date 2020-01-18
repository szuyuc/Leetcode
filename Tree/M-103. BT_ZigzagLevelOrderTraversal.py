class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        
        if not root:
            return None
        
        stack = [root]
        flag = 1
        zigzag = []
        while stack: 
            temp_node = []
            for node in stack: 
                if node.left:
                    temp_node.append(node.left)
                if node.right:
                    temp_node.append(node.right)
            temp = [node.val for node in stack[::flag]]
            zigzag.append(temp)
            flag*=-1
            if len(temp_node) != 0:
                stack = temp_node
            else:
                return zigzag
        