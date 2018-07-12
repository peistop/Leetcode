"""
345. Reverse Vowels of a String
https://leetcode.com/problems/reverse-vowels-of-a-string

Easy: 99.00%
Testcase Example: "hello"


"""

class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = "aeiouAEIOU"

        s = list(s)
        left = 0
        right = len(s) - 1
        while left < right:
            if s[right] in vowels and s[left] in vowels:
                s[right], s[left] = s[left], s[right]
                right -= 1
                left += 1
            if s[left] not in vowels:
                left += 1
            if s[right] not in vowels:
                right -= 1
           
        return "".join(s) 
            

if __name__ == "__main__":
    solution = Solution()
    s = "leetcode"
    print(solution.reverseVowels(s))
            
                
            
