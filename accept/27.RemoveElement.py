"""
27. Remove Element

TestCase Example: [3,2,2,3]\n3
"""
class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        start = 0
        end = len(nums) - 1
        while start <= end:
            if nums[start] == val:
                nums[start], nums[end] = nums[end], nums[start]
                end -= 1
            else:
                start += 1
        nums = nums[:start]
        return nums, start

if __name__ == "__main__":
    solution = Solution()
    nums = [3,2,2,3]
    val = 3
    print(solution.removeElement(nums, val))