"""
661. Image Smoother

Easy: 49.60

Given a 2D integer matrix M representing the gray scale of an 
image, you need to design a smoother to make the gray scale of 
each cell becomes the average gray scale (rounding down) of all 
the 8 surrounding cells and itself. If a cell has less than 8 
surrounding cells, then use as many as you can.

Example 1:
Input:
[[1,1,1],
 [1,0,1],
 [1,1,1]]
Output:
[[0, 0, 0],
 [0, 0, 0],
 [0, 0, 0]]
Explanation:
For the point (0,0), (0,2), (2,0), (2,2): floor(3/4) = floor(0.75) = 0
For the point (0,1), (1,0), (1,2), (2,1): floor(5/6) = floor(0.83333333) = 0
For the point (1,1): floor(8/9) = floor(0.88888889) = 0
"""
from copy import deepcopy
class Solution:
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        m = len(M)
        n = len(M[0]) if m else 0
        res = deepcopy(M)
        for i in range(m):
            for j in range(n):
                neighbors = [
                    M[x][y]
                    for x in [i-1, i, i+1]
                    for y in [j-1, j, j+1]
                    if 0 <= x < m and 0 <= y < n
                ]
                res[i][j] = sum(neighbors)//len(neighbors)
        return res

if __name__ == "__main__":
    solution = Solution()
    M = [[1,1,1],[1,0,1],[1,1,1]]
    print(solution.imageSmoother(M))