"""
383. Ransom Note
https://leetcode.com/problems/ransom-note/

Easy: 83.82%
Testcase Example: "a"\n"b"

Given an arbitrary ransom note string and another string containing 
letters from all the magazines, write a function that will return 
true if the ransom note can be constructed from the magazines ; 
otherwise, it will return false.

Each letter in the magazine string can only be used once in your 
ransom note.

Note:
You may assume that both strings contain only lowercase letters.

canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true

"""
class Solution:
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        note = list(ransomNote)
        m = list(magazine)
        for word in note:
            if word in m:
                m.remove(word)
            else:
                return False
        return True

if __name__ == "__main__":
    solution = Solution()
    note = "aba"
    magazine = "aaba"
    print(solution.canConstruct(note, magazine))
        