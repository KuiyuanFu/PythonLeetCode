# @lc app=leetcode id=746 lang=python3
#
# [746] Min Cost Climbing Stairs
#
# https://leetcode.com/problems/min-cost-climbing-stairs/description/
#
# algorithms
# Easy (54.38%)
# Likes:    4630
# Dislikes: 889
# Total Accepted:    335.8K
# Total Submissions: 600K
# Testcase Example:  '[10,15,20]'
#
# You are given an integer array cost where cost[i] is the cost of i^th step on
# a staircase. Once you pay the cost, you can either climb one or two steps.
#
# You can either start from the step with index 0, or the step with index 1.
#
# Return the minimum cost to reach the top of the floor.
#
#
# Example 1:
#
#
# Input: cost = [10,15,20]
# Output: 15
# Explanation: You will start at index 1.
# - Pay 15 and climb two steps to reach the top.
# The total cost is 15.
#
#
# Example 2:
#
#
# Input: cost = [1,100,1,1,1,100,1,1,100,1]
# Output: 6
# Explanation: You will start at index 0.
# - Pay 1 and climb two steps to reach index 2.
# - Pay 1 and climb two steps to reach index 4.
# - Pay 1 and climb two steps to reach index 6.
# - Pay 1 and climb one step to reach index 7.
# - Pay 1 and climb two steps to reach index 9.
# - Pay 1 and climb one step to reach the top.
# The total cost is 6.
#
#
#
# Constraints:
#
#
# 2 <= cost.length <= 1000
# 0 <= cost[i] <= 999
#
#
#

# @lc tags=trie

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 每个台阶有一个代价，付钱后可以爬一或二层。求最少的花费。
# dp。添加最后一个台阶，代价为0，每一层台阶加上前两个台阶的最小值。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        cost.append(0)
        for i in range(2, len(cost)):
            cost[i] += min(cost[i - 1], cost[i - 2])
        return cost[-1]
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('cost = [10,15,20]')
    print('Exception :')
    print('15')
    print('Output :')
    print(str(Solution().minCostClimbingStairs([10, 15, 20])))
    print()

    print('Example 2:')
    print('Input : ')
    print('cost = [1,100,1,1,1,100,1,1,100,1]')
    print('Exception :')
    print('6')
    print('Output :')
    print(
        str(Solution().minCostClimbingStairs(
            [1, 100, 1, 1, 1, 100, 1, 1, 100, 1])))
    print()

    pass
# @lc main=end