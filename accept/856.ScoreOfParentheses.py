"""
856. Score of Parentheses

# stack

Meduim:
Testcase Example: ()

Given a balanced parentheses string S, compute the score of the string 
based on the following rule:

() has score 1
AB has score A + B, where A and B are balanced parentheses strings.
(A) has score 2 * A, where A is a balanced parentheses string.
 

Example 1:

Input: "()"
Output: 1

Example 2:

Input: "(())"
Output: 2

Example 3:

Input: "()()"
Output: 2

Example 4:

Input: "(()(()))"
Output: 6

Note:

1. S is a balanced parentheses string, containing only ( and ).
2. 2 <= S.length <= 50

"""

class Solution:
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        stack = []
        res = 0
        for c in S:
            if c == "(":
                stack.append(0)
            else:
                last = stack.pop()
                tmp = last and last * 2 or 1
                if stack:
                    stack[-1] += tmp
                else:
                    res += tmp
        return res

if __name__ == "__main__":
    solution = Solution()
    S1 = "()"
    print(solution.scoreOfParentheses(S1))
    S2 = "(()(()))"
    print(solution.scoreOfParentheses(S2))
