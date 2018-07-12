"""
541. Reverse String II

Easy: 93.44%
Testcase Exmple: "abcdefg"\n2

iven a string and an integer k, you need to reverse the first k 
characters for every 2k characters counting from the start of 
the string. If there are less than k characters left, reverse all 
of them. If there are less than 2k but greater than or equal to 
k characters, then reverse the first k characters and left the 
other as original.

Example:
Input: s = "abcdefg", k = 2
Output: "bacdfeg"
"""
class Solution:
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        s = list(s)
        for i in range(0, len(s), 2*k):
            s[i:i+k] = reversed(s[i:i+k])
        return "".join(s)

if __name__ == "__main__":
    solution = Solution()
    s, k = "abcdefg", 2
    print(solution.reverseStr(s, k))
