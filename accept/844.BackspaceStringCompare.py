"""
844. Backspace String Compare

Easy: 100%

Given two strings S and T, return if they are equal when both are 
typed into empty text editors. # means a backspace character.

Example 1:

Input: S = "ab#c", T = "ad#c"
Output: true

Explanation: Both S and T become "ac".

Example 2:

Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".

Example 3:

Input: S = "a##c", T = "#a#c"
Output: true
Explanation: Both S and T become "c".

Example 4:

Input: S = "a#c", T = "b"
Output: false
Explanation: S becomes "c" while T becomes "b".

Follow up:
Can you solve it in O(N) time and O(1) space?
"""
class Solution:
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        S, T = list(S), list(T)
        sLen, tLen = len(S), len(T)
        for i in range(sLen):
            if S[i] != "#":
                T.append(S[i])
            elif len(T) > tLen and S[i] == "#":
                T.pop()
        for i in range(tLen):
            if T[i] != "#":
                S.append(T[i])
            elif len(S) > sLen and T[i] == "#":
                S.pop()
        return "".join(S[sLen:]) == "".join(T[sLen:])

if __name__ == "__main__":
    solution = Solution()
    S = "ab#c"
    T = "ad#c"
    print(solution.backspaceCompare(S, T))
    S = "a##c"
    T = "#a#c"
    print(solution.backspaceCompare(S, T))
