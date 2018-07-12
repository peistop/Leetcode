"""
657. Judge Route Circle
https://leetcode.com/problems/judge-route-circle

Easy: 93.94%
Testcase Example: "UD"

Initially, there is a Robot at position (0, 0). Given a sequence 
of its moves, judge if this robot makes a circle, which means it 
moves back to the original place.

The move sequence is represented by a string. And each move is 
represent by a character. The valid robot moves are R (Right), 
L (Left), U (Up) and D (down). The output should be true or false 
representing whether the robot makes a circle.

Example 1:
Input: "UD"
Output: true

Example 2:
Input: "LL"
Output: false
"""

class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        vertical = moves.count("U") - moves.count("D")
        horizon = moves.count("R") - moves.count("L")
        return vertical == 0 and horizon == 0

if __name__ == "__main__":
    solution = Solution()
    input1 = "UD"
    input2 = "LL"
    print(solution.judgeCircle(input1))
    print(solution.judgeCircle(input2))
