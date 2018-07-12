"""
387. First Unique Character in a String
https://leetcode.com/problems/first-unique-character-in-a-string

Easy: 99.76%
Testcase Example: "leetcode"

Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
"""
class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0: return -1
        if len(s) == 1: return 0

        letters = "abcdefghijklmnopqrstuvwxyz"
        freq = [s.index(l) for l in letters if s.count(l) == 1]
        if len(freq) > 0:
            return min(freq)
        return -1

if __name__ == "__main__":
    solution = Solution()
    input = "leetcode"
    print(solution.firstUniqChar(input))