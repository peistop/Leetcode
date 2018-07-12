"""
696. Count Binary Substrings
https://leetcode.com/problems/count-binary-substrings

Easy: 41.73%
Testcase Example: "00110"

Give a string s, count the number of non-empty (contiguous) 
substrings that have the same number of 0's and 1's, and all 
the 0's and all the 1's in these substrings are grouped 
consecutively.

Substrings that occur multiple times are counted the number 
of times they occur.


Example 1:

Input: "00110011"
Output: 6

Example 2:

Input: "10101"
Output: 4

"""

class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        consCount = []
        count = 1
        for i, c in enumerate(s):
            if s[i] == s[i-1]:
                count += 1
            else:
                consCount.append(count)
                count = 1
        consCount.append(count) # for last one
        count = 0
        for i in range(1, len(consCount)):
            count += min([consCount[i], consCount[i-1]])
        return count

if __name__ == "__main__":
    solution = Solution()
    input = "00110"
    print(solution.countBinarySubstrings(input))
