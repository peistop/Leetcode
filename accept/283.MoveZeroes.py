"""
283. Move Zeroes
https://leetcode.com/problems/move-zeroes/description/

Easy: 99.33%
Testcase Example: [0,1,0,3,12]

Given an array nums, write a function to move all 0's to the end of it 
while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]

Note:
You must do this in-place without making a copy of the array.
"""

class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        write = 0
        for num in nums:
            if num != 0:
                nums[write] = num
                write += 1
        nums[write:] = [0] * (len(nums) - write)
        return nums

if __name__ == "__main__":
    solution = Solution()
    nums = [0,1,0,3,12]
    print(solution.moveZeroes(nums))
                