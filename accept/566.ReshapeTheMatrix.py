"""
566. Reshape the Matrix
https://leetcode.com/problems/reshape-the-matrix/

Easy: 88.52%
Testcase Example: A = [[1,2],[3,4]]\n1\n4

You're given a matrix represented by a two-dimensional array, and two 
positive integers r and c representing the row number and column number of 
the wanted reshaped matrix, respectively.

The reshaped matrix need to be filled with all the elements of the original 
matrix in the same row-traversing order as they were.

If the 'reshape' operation with given parameters is possible and legal, 
output the new reshaped matrix; Otherwise, output the original matrix.

Example 1:
Input: 
nums = 
[[1,2],
 [3,4]]
r = 1, c = 4
Output: 
[[1,2,3,4]]

Example 2:
Input: 
nums = 
[[1,2],
 [3,4]]
r = 2, c = 4
Output: 
[[1,2],
 [3,4]]
Explanation:
There is no way to reshape a 2 * 2 matrix to a 2 * 4 matrix. 
So output the original matrix.

"""

import numpy as np
class Solution:
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """

        
        if r * c != len(nums) * len(nums[0]):
            return nums

        # use numpy, slow
        #arr = np.array(nums)
        #return arr.reshape(r, c).tolist()
        
        res = [[0 for _ in range(c)] for _ in range(r)] 
        col = 0
        row = 0
        for i in range(len(nums)):
            for j in range(len(nums[0])):
                res[row][col] = nums[i][j]
                col += 1
                if col >= c:
                    col = 0
                    row += 1
        return res
    
solution = Solution()
A = [[1,2],[3,4]]
r, c = 1, 4
print(solution.matrixReshape(A, r, c))