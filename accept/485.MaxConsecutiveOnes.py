"""
485. Max Consecutive Ones

Easy:
Testcase Example: [1,0,1,1,0,1]

Given a binary array, find the maximum number of consecutive 1s 
in this array.

Example 1:
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are 
consecutive 1s. The maximum number of consecutive 1s is 3.

"""

class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        sumup, Max = 0, 0
        for i in nums:
            if i == 1:
                sumup += 1
            else:
                if sumup > Max:
                    Max = sumup
                sumup = 0
        return Max

if __name__ == "__main__":
    solution = Solution()
    nums = [1,0,1,1,0,1]
    print(solution.findMaxConsecutiveOnes(nums))