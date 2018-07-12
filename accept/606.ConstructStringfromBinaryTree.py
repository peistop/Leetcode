"""
606. Construct String from Binary Tree
https://leetcode.com/problems/construct-string-from-binary-tree

Easy: 100%
Testcase Example: [1,2,3,4]

You need to construct a string consists of parenthesis and 
integers from a binary tree with the preorder traversing way.

The null node needs to be represented by empty parenthesis 
pair "()". And you need to omit all the empty parenthesis 
pairs that don't affect the one-to-one mapping relationship 
between the string and the original binary tree.

Input: Binary tree: [1,2,3,4]
       1
     /   \
    2     3
   /    
  4     

Output: "1(2(4))(3)"

Explanation: Originallay it needs to be "1(2(4)())(3()())", 
but you need to omit all the unnecessary empty parenthesis pairs. 
And it will be "1(2(4))(3)".
"""

import TreeNode

class Solution:
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        if not t.val:
              return ""
        result = str(t.val)
        if t.left:
              result += "(" + self.tree2str(t.left) + ")"
              if t.right:
                    result += "(" + self.tree2str(t.right) + ")"
        elif t.right:
              result += "()" + "(" + self.tree2str(t.right) + ")"
        return result

if __name__ == "__main__":
      solution = Solution()
      input = TreeNode.createTreeNode([1,2,3,4])
      print(solution.tree2str(input))
                    
        
        

