"""
551. Student Attendance Record I
https://leetcode.com/problems/student-attendance-record-i

Easy: 88.97%
Testcase example: "PPALLP"

You are given a string representing an attendance record for a 
student. The record only contains the following three characters:
'A' : Absent.
'L' : Late.
'P' : Present.
A student could be rewarded if his attendance record doesn't 
contain more than one 'A' (absent) or more than two continuous 
'L' (late).

You need to return whether the student could be rewarded according 
to his attendance record.

Example 1:

Input: "PPALLP"
Output: True

Example 2:

Input: "PPALLL"
Output: False
"""

class Solution:
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        if s.count("A") <= 1 and s.count("LLL") == 0:
            return True
        return False

if __name__ == "__main__":
    solution = Solution()
    s = "PPALLP"
    print(solution.checkRecord(s))