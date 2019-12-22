class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        
        """
        pseudocode
        for num in nums:
            if num < prev_num:
                prev_num.right = num
            if num > prev_num:
            num.left = prev_num 
        """
        

        stack = []
        
        for num in nums:
            node = TreeNode(num) # build a node 
 
            while stack and stack[-1].val<=num:
                node.left = stack.pop()
            if stack and stack[-1].val>num:
                stack[-1].right = node
            stack.append(node)
      
        return stack[0]

    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:

        """
        Same approach as convert an array to a tree
        Time Complexity: O(N2)
        """
        def grow_tree(arr):
            if len(arr) == 0:
                return None
            
            max_ind = -1
            max_val = -float('inf')
            for ind, val in enumerate(arr):
                if val>max_val:
                    max_val = val 
                    max_ind = ind 
            
            node = TreeNode(max_val)
            node.left = grow_tree(arr[:max_ind])
            if max_ind+1 < len(arr):
                node.right = grow_tree(arr[max_ind+1:])
            
            return node
        return grow_tree(nums)