class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        """
        state transition 
        prev = sell or cold or buy or not doing anything 
        today = cold or but or sell or not doing or buy 
        
        hold/buy -> hold
        hold/buy -> sell
        hold/sell -> hold 
        
        s0 has nothing
        s1 has something
        s2 sell 

        """

        # init 
        s0 = 0
        s1 = -float('inf')
        s2 = 0
        
        for price in prices:
            # get s1 current state
            old_s1 = s1
            s1 = max(s1,s0-price)
            # get s0 current state from old s0 or from sell(s2)
            s0 = max(s0,s2)
            # get prev total asset and include the current one
            s2 = price + old_s1
            
        return max(s0,s2)
            