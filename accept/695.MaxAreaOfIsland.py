"""
695. Max Area of Island

Easy: 68.52%
Testcase Example: [[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]

Given a non-empty 2D array grid of 0's and 1's, an island is a group 
of 1's (representing land) connected 4-directionally (horizontal or 
vertical.) You may assume all four edges of the grid are surrounded 
by water.

Find the maximum area of an island in the given 2D array. (If there 
is no island, the maximum area is 0.)

Example 1:

[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
Given the above grid, return 6. Note the answer is not 11, because the 
island must be connected 4-directionally.
"""

class Solution:
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def dfs(i, j):
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j]:
                grid[i][j] = 0
                return 1 + dfs(i-1, j) + dfs(i, j-1) + dfs(i+1, j) + dfs(i, j+1)
            return 0
        
        areas = [dfs(i, j) for i in range(len(grid)) for j in range(len(grid[0]))]
        return max(areas)

if __name__ == "__main__":
    grid = [[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]
    solution = Solution()
    print(solution.maxAreaOfIsland(grid))
        
        