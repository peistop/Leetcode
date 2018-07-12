"""
448. Find All Numbers Disappeared in an Array
https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array

Easy: 98.10%
Testcase Example: [4,3,2,7,8,2,3,1]

Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some 
elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the 
returned list does not count as extra space.

Example:

Input: [4,3,2,7,8,2,3,1]
Output: [5,6]
"""

class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        flags = [0 for _ in range(len(nums))]
        for num in nums:
            flags[num-1] = 1
        res = [i+1 for i, num in enumerate(flags) if num == 0]
        return res

if __name__ == "__main__":
    nums = [4,3,2,7,8,2,3,1]
    solution = Solution()
    print(solution.findDisappearedNumbers(nums))


