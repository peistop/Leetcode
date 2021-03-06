"""
503. Next Greater Element II

Given a circular array (the next element of the last element is 
the first element of the array), print the Next Greater Number 
for every element. The Next Greater Number of a number x is the 
first greater number to its traversing-order next in the array, 
which means you could search circularly to find its next greater 
number. If it doesn't exist, output -1 for this number.

Example 1:

Input: [1,2,1]
Output: [2,-1,2]
Explanation: The first 1's next greater number is 2; 
The number 2 can't find next greater number; 
The second 1's next greater number needs to search circularly, 
which is also 2.
"""
class Solution:
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        stack = [i for i in range(len(nums))]
        res = [-1] * len(nums)
        for i in range(len(nums)):
            while stack and nums[i] > nums[stack[-1]]:
                res[stack.pop()] = nums[i]
            stack.append(i)
        return res


if __name__ == "__main__":
    solution = Solution()
    nums = [1,2,1]
    print(solution.nextGreaterElements(nums))
