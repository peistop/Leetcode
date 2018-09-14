"""
739. Daily Temperatures
https://leetcode.com/problems/daily-temperatures/

Medium:
Testcase Example: [73, 74, 75, 71, 69, 72, 76, 73]

Given a list of daily temperatures, produce a list that, for each day in 
the input, tells you how many days you would have to wait until a warmer 
temperature. If there is no future day for which this is possible, put 0 
instead.

For example, given the list temperatures = [73, 74, 75, 71, 69, 72, 76, 73], 
your output should be [1, 1, 4, 2, 1, 1, 0, 0].

Note: The length of temperatures will be in the range [1, 30000]. Each 
temperature will be an integer in the range [30, 100].
"""
class Solution:
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        # keep a stack of indices such that T[stack[-1]] < T[stack[-2]] < ..., 
        # where stack[-1] is the top of the stack.

        stack = [] # index of T from hottest to coldest
        res = [0] * len(temperatures)
        for i in range(len(temperatures)-1, -1, -1):
            while stack and temperatures[stack[-1]] <= temperatures[i]:
                stack.pop()
            if stack:
                res[i] = stack[-1] - i
            stack.append(i)
        return res

if __name__ == "__main__":
    solution = Solution()
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    print(solution.dailyTemperatures(temperatures))
 