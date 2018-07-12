"""
697. Degree of an Array

Easy:

Given a non-empty array of non-negative integers nums, the degree 
of this array is defined as the maximum frequency of any one of 
its elements.

Your task is to find the smallest possible length of a (contiguous) 
subarray of nums, that has the same degree as nums.

Example 1:
Input: [1, 2, 2, 3, 1]
Output: 2
Explanation: 
The input array has a degree of 2 because both elements 1 and 2 
appear twice.
Of the subarrays that have the same degree:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], 
[2, 2]
The shortest length is 2. So return 2.

Example 2:
Input: [1,2,2,3,1,4,2]
Output: 6
"""
import collections

class Solution:
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start, end = {}, {}
        for i, num in enumerate(nums):
            start.setdefault(num, i)
            end[num] = i
        counters = collections.Counter(nums)
        Max = max(counters.values())
        print(counters, Max)
        return min([end[u] - start[u] for u in counters if counters[u] == Max]) + 1

if __name__ == "__main__":
    solution = Solution()
    nums = [1,2,2,3,1]
    print(solution.findShortestSubArray(nums))
