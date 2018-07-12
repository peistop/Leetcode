"""
459. Repeated Substring Pattern

Easy: 98.99%
Testcase Example: "abab"

Given a non-empty string check if it can be constructed by taking
a substring of it and appending multiple copies of the substring 
together. You may assume the given string consists of lowercase 
English letters only and its length will not exceed 10000.

Example 1:

Input: "abab"
Output: True
Explanation: It's the substring "ab" twice.

Example 2:

Input: "aba"
Output: False
"""

class Solution:
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: 
        """

        """
        Basic idea:
        1. s[0] is the first char of repeated substring
        2. s[-1] is the last char of repeated substring
        """
        ss = s + s
        return s in ss[1:len(ss)-1]
        # idx = ss.index(s)
        # repeated_substring = s[0: idx]

if __name__ == "__main__":
    solution = Solution()
    s = "abcabca"
    print(solution.repeatedSubstringPattern(s))
