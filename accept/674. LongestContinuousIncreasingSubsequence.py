

class Solution:
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        count, Max = 1, 1
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] > 0:
                count += 1
            else:
                if count > Max:
                    Max = count
                count = 1
                
        return max([count, Max])