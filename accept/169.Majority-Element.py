"""
169. Majority Element
https://leetcode.com/problems/majority-element/description/

"""
class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        for num in set(nums):
            if nums.count(num) > len(nums) // 2:
                return num
        