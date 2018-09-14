"""
144. Binary Tree Preorder Traversal

Given a binary tree, return the preorder traversal of its 
nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,2,3]
Follow up: Recursive solution is trivial, could you do it 
iteratively?
"""

from utils.TreeNode import TreeNode, createTreeNode
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        stack = []
        while stack or root:
            while root:
                stack.append(root)
                res.append(root.val)
                root = root.left
            tmp = stack.pop()
            root = tmp.right
        return res

if __name__ == "__main__":
    solution = Solution()
    arr = [1, None, 2, 3]
    root = createTreeNode(arr)
    print(solution.preorderTraversal(root))