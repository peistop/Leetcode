"""
665. Non-decreasing Array

Easy: 100%
Testcase Example: [4,2,3]

Given an array with n integers, your task is to check if it could 
become non-decreasing by modifying at most 1 element.

We define an array is non-decreasing if array[i] <= array[i + 1] 
holds for every i (1 <= i < n).

Example 1:

Input: [4,2,3]
Output: True
Explanation: You could modify the first 4 to 1 to get a non-decreasing 
array.

Example 2:

Input: [4,2,1]
Output: False
Explanation: You can't get a non-decreasing array by modify at most 
one element.

Note: The n belongs to [1, 10,000].
"""
class Solution:
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dec_count = 0
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                dec_count += 1
                if i == 0:
                    nums[i] = nums[i+1]
                elif nums[i-1] > nums[i+1]:
                    nums[i+1] = nums[i]
                else:
                    nums[i] = nums[i+1]
            if dec_count > 1:
                return False
        return True

if __name__ == "__main__":
    solution = Solution()
    nums = [4,2,3]
    print(solution.checkPossibility(nums))
    nums = [-1, 4, 2, 3]
    print(solution.checkPossibility(nums))
    nums = [3, 4, 2, 3]
    print(solution.checkPossibility(nums))