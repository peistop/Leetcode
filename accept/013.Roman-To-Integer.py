"""
13. Roman to Integer
https://leetcode.com/problems/roman-to-integer/description/

Easy: 95.09%
Testcase Example: "III"

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer. 
Input is guaranteed to be within the range from 1 to 3999.

Example 1:

Input: "LVIII"
Output: 58

Example 2:

Input: "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
"""
class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        res = 0
        s = s[::-1]
        count = dic[s[0]]
        
        for i in range(1, len(s)):
            if s[i] == "I" and (s[i-1] == "V" or s[i-1] == "X"):
                count -= 1
            elif s[i] == "X" and (s[i-1] == "L" or s[i-1] == "C"):
                count -= 10
            elif s[i] == "C" and (s[i-1] == "D" or s[i-1] == "M"):
                count -= 100
            else:
                count += dic[s[i]]
        return count

if __name__ == "__main__":
    solution = Solution()
    input = "MCMXCIV"
    print(solution.romanToInt(input))
            
