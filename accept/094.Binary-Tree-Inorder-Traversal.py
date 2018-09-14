"""
94. Binary Tree Inorder Traversal

Medium: 47.35%
Testcase Example: [1,null,2,3]

Given a binary tree, return the inorder traversal of its 
nodes' values.

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

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from utils.TreeNode import TreeNode, createTreeNode

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            tmp = stack.pop()
            res.append(tmp.val)
            root = tmp.right
        return res

if __name__ == "__main__":
    try:
        solution = Solution()
        arr = [1, None, 2, 3]
        root = createTreeNode(arr)
        print(solution.inorderTraversal(root))
    except:
        pass