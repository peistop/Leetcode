"""
832. Flipping an Image
https://leetcode.com/problems/flipping-an-image/description/

Easy: 99.9%
Testcase Example: [[1,1,0],[1,0,1],[0,0,0]]

Given a binary matrix A, we want to flip the image horizontally, 
then invert it, and return the resulting image.

To flip an image horizontally means that each row of the image is 
reversed.  For example, flipping [1, 1, 0] horizontally results 
in [0, 1, 1].

To invert an image means that each 0 is replaced by 1, and each 1 
is replaced by 0. For example, inverting [0, 1, 1] results in [1, 0, 0].

Example 1:

Input: [[1,1,0],[1,0,1],[0,0,0]]
Output: [[1,0,0],[0,1,0],[1,1,1]]
Explanation: First reverse each row: [[0,1,1],[1,0,1],[0,0,0]].
Then, invert the image: [[1,0,0],[0,1,0],[1,1,1]]

Example 2:

Input: [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
Output: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
"""
class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        return [[1-i for i in row[::-1]] for row in A]
        
        #for i in range(len(A)):
        #    A[i] = A[i][::-1]
        #    for j in range(len(A[0])):
        #        if A[i][j] == 1: A[i][j] = 0
        #        else: A[i][j] = 1
        #        
        #return A

if __name__ == "__main__":
    solution = Solution()
    A = [[1,1,0],[1,0,1],[0,0,0]]
    print(solution.flipAndInvertImage(A))