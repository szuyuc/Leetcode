import copy 
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        if not obstacleGrid or obstacleGrid[0][0] == 1 :
            return 0
        
        col_num = len(obstacleGrid[0])
        row_num = len(obstacleGrid)
        
        paths = [[0 for j in range(col_num) ] for i in range(row_num) ]
        paths[0][0] = 1
        for row in range(row_num):
            for col in range(col_num):
                
                if obstacleGrid[row][col]== 1:
                    paths[row][col]= 0 
                else: 
                    if row == 0 and col> 0 : 
                        paths[0][col] = paths[0][col-1]
                    if col == 0 and row> 0 : 
                        paths[row][0] = paths[row-1][0]
                    else :
                        if row!=0 and col != 0 :
                            paths[row][col] = paths[row-1][col]+paths[row][col-1]
              
        return paths[-1][-1]    