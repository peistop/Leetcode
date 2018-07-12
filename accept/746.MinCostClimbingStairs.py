"""
746. Min Cost Climbing Stairs

"""
class Solution:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        if len(cost) <= 1:
            return 0

        dp = [0] * len(cost)
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2, len(cost)):
            dp[i] = min(dp[i-1] + cost[i], dp[i-2] + cost[i])
        return min(dp[-1], dp[-2])

if __name__ == "__main__":
    cost = [10, 15, 20]
    solution = Solution()
    print(solution.minCostClimbingStairs(cost))
