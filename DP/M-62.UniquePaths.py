class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        paths = []
        
        if m<=1 and n<=1:
            return 1
        
        for row in range(n):
            for col in range(m):
                if col == 0 and row == 0:
                    paths.append([0])
                elif col == 0:
                    paths.append([1])
                elif row == 0:
                    paths[row].append(1)
                else:
                    paths[row].append(paths[row-1][col]+paths[row][col-1]) 
        return paths[n-1][m-1]
                    
        """
        Sol2:
        # init 
        paths = [[1 for i in range(m)] for j in range(n)]
        for row in range(1,n):
            for col in range(1,m):
            paths[row][col] = ...
        
        """
