"""
344. Reverse String
https://leetcode.com/problems/reverse-string/

Easy: 97.49%
Testcase Example: "hello"

Write a function that takes a string as input and returns the string reversed.

Example:
Given s = "hello", return "olleh".
"""
class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]
        
        # l = len(s)
        # if l < 2:
        #     return s
        # return self.reverseString(s[l//2:]) + self.reverseString(s[:l//2])

if __name__ == "__main__":
    solution = Solution()
    input = "hello"
    print(solution.reverseString(input))



