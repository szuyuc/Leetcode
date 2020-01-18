class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        
        max_area = 0
        lp = 0
        rp = len(height)-1
        
        while lp <rp:
            """
            The max area we can get from the two pointers is smaller*(right-left).
            Then, max(older_max, cur_max)
            Moving the smaller forward to see if we can get a bigger value.
            
            """
            max_area = max(max_area,min(height[lp],height[rp])*(rp-lp))
            if height[lp] <= height[rp]:
                lp+=1
            else:
                rp-=1
        return max_area
        
                
                
            
        
        """
        Brute Force
        
        max_num = 0 
        for ind, num in enumerate(height):
            for innerind in range(ind+1,len(height)):
                small = min(height[innerind],num) 
                max_num = max(small*(innerind-ind),max_num)
                
                
                
        return max_num
        """