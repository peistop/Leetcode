"""
830. Positions of Large Groups

In a string S of lowercase letters, these letters form consecutive 
groups of the same character.
For example, a string like S = "abbxxxxzyy" has the groups "a", "bb", 
"xxxx", "z" and "yy".

Call a group large if it has 3 or more characters.  We would like 
the starting and ending positions of every large group.

The final answer should be in lexicographic order.

Example 1:

Input: "abbxxxxzzy"
Output: [[3,6]]
Explanation: "xxxx" is the single large group with starting 3 and 
ending positions 6.

Example 2:

Input: "abc"
Output: []
Explanation: We have "a","b" and "c" but no large group.

Example 3:

Input: "abcdddeeeeaabbbcd"
Output: [[3,5],[6,9],[12,14]]
"""
class Solution:
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        count = 1
        start = 0
        res = []
        for i in range(1, len(S)):
            if S[i] == S[i-1]:
                count += 1
            else:
                if count >= 3:
                    res.append([start, i-1])
                start = i
                count = 1
        if count >= 3:
            res.append([start, len(S)-1])
        return res

if __name__ == "__main__":
    solution = Solution()
    S = "abbxxxxzzy"
    print(solution.largeGroupPositions(S))
