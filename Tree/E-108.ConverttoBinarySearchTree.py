class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:

        """
        Grow tree using recursive 
        Time complexity: O(N)
        Space complexity: O(N). O(N) keep the output. O(logN) for recursion stack 
        """
    
        def traverse(arr):
            if len(arr)==0:
                return None
            ind = len(arr)//2 
            # ind = 2 val = 0
            
            node = TreeNode(arr[ind])
            node.left = traverse(arr[:ind]) #[-10,-3]
            if ind+1 < len(arr):
                node.right =  traverse(arr[ind+1:]) # [5,9]
                                 
            return node                     
        return traverse(nums)
            
