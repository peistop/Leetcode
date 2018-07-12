"""
868. Transpose Matrix
https://leetcode.com/problems/transpose-matrix/description/

Easy
Testcase Example: [[1,2,3],[4,5,6],[7,8,9]]

Given a matrix A, return the transpose of A.
The transpose of a matrix is the matrix flipped over it's main diagonal, 
switching the row and column indices of the matrix.

Example 1:

Input: [[1,2,3],[4,5,6],[7,8,9]]
Output: [[1,4,7],[2,5,8],[3,6,9]]

Example 2:

Input: [[1,2,3],[4,5,6]]
Output: [[1,4],[2,5],[3,6]]
 
"""
class Solution:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        return [[A[i][j] for i in range(len(A))] for j in range(len(A[0]))]

if __name__ == "__main__":
    solution = Solution()
    A = [[1,2,3],[4,5,6],[7,8,9]]
    print(solution.transpose(A))
    A = [[1,2,3],[4,5,6]]
    print(solution.transpose(A))