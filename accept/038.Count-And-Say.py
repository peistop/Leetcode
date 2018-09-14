"""
38. Count and Say
https://leetcode.com/problems/count-and-say

Easy: 98.37%
Testcase Example: "1"


The count-and-say sequence is the sequence of integers with the 
first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth term of the count-and-say 
sequence.

Note: Each term of the sequence of integers will be represented 
as a string.

Example 1:

Input: 1
Output: "1"

Example 2:

Input: 4
Output: "1211"
"""

class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        result = "1"
        for _ in range(1, n):
            let = result[0]
            count = 1
            tmp = ""
            for s in result[1:]:
                if s == let:
                    count += 1
                else:
                    tmp += str(count) + let
                    let = s
                    count = 1
            tmp += str(count) + let
            result = tmp
        return result

if __name__ == "__main__":
    solution = Solution()
    n = 4
    print(solution.countAndSay(5))
                    
                