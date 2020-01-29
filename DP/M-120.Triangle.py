class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        if not triangle or triangle[0][0] == None:
            return 0
        if len(triangle) ==1 :
            return triangle[0][0]
        
        for row in range(1, len(triangle)):
            for ind in range(len(triangle[row])):
                if ind==0 :
                    triangle[row][ind]+= triangle[row-1][0]   
                elif ind == len(triangle[row])-1:
                    triangle[row][ind]+= triangle[row-1][-1]                       
                else:
                    triangle[row][ind]+= min(triangle[row-1][ind],triangle[row-1][ind-1])
        print(triangle)
        return min(triangle[-1])
        
        """
        inplace 
        [2]
        [3+2 4+2]
        [11 min(5+5,5+6)  7+6 ]
        
        """ 