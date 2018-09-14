"""
94. Binary Tree Inorder Traversal

Given a binary tree, return the inorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]

Follow up: 
Recursive solution is trivial, could you do it iteratively?
"""

from utils.TreeNode import TreeNode, createTreeNode

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        

if __name__ == "__main__":
    solution = Solution()
    arr = [1, None, 2, 3]
    root = createTreeNode(arr)
    print(solution.inorderTraversal(root))