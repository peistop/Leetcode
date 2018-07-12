"""
557. Reverse Words in a String III
https://leetcode.com/problems/reverse-words-in-a-string-iii

Easy: 98.40%
Testcase Example: "Let's take LeetCode contest"

Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Example 1:
Input: "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
"""
class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        sList = s.split()
        res = []
        for word in sList:
            res.append(word[::-1])
        return " ".join(res)

if __name__ == "__main__":
    solution = Solution()
    input = "Let's take LeetCode contest"
    print(solution.reverseWords(input))
        