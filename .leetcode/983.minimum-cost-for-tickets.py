# @lc app=leetcode id=983 lang=python3
#
# [983] Minimum Cost For Tickets
#
# https://leetcode.com/problems/minimum-cost-for-tickets/description/
#
# algorithms
# Medium (64.37%)
# Likes:    5123
# Dislikes: 85
# Total Accepted:    172K
# Total Submissions: 267.3K
# Testcase Example:  '[1,4,6,7,8,20]\n[2,7,15]'
#
# You have planned some train traveling one year in advance. The days of the
# year in which you will travel are given as an integer array days. Each day is
# an integer from 1 to 365.
#
# Train tickets are sold in three different ways:
#
#
# a 1-day pass is sold for costs[0] dollars,
# a 7-day pass is sold for costs[1] dollars, and
# a 30-day pass is sold for costs[2] dollars.
#
#
# The passes allow that many days of consecutive travel.
#
#
# For example, if we get a 7-day pass on day 2, then we can travel for 7 days:
# 2, 3, 4, 5, 6, 7, and 8.
#
#
# Return the minimum number of dollars you need to travel every day in the
# given list of days.
#
#
# Example 1:
#
#
# Input: days = [1,4,6,7,8,20], costs = [2,7,15]
# Output: 11
# Explanation: For example, here is one way to buy passes that lets you travel
# your travel plan:
# On day 1, you bought a 1-day pass for costs[0] = $2, which covered day 1.
# On day 3, you bought a 7-day pass for costs[1] = $7, which covered days 3, 4,
# ..., 9.
# On day 20, you bought a 1-day pass for costs[0] = $2, which covered day 20.
# In total, you spent $11 and covered all the days of your travel.
#
#
# Example 2:
#
#
# Input: days = [1,2,3,4,5,6,7,8,9,10,30,31], costs = [2,7,15]
# Output: 17
# Explanation: For example, here is one way to buy passes that lets you travel
# your travel plan:
# On day 1, you bought a 30-day pass for costs[2] = $15 which covered days 1,
# 2, ..., 30.
# On day 31, you bought a 1-day pass for costs[0] = $2 which covered day 31.
# In total, you spent $17 and covered all the days of your travel.
#
#
#
# Constraints:
#
#
# 1 <= days.length <= 365
# 1 <= days[i] <= 365
# days is in strictly increasing order.
# costs.length == 3
# 1 <= costs[i] <= 1000
#
#
#

# @lc tags=stack

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 可以买1，7，30天的票，要覆盖所有给定日期。
# dp。存储当前日期最少代价，之后对每个票，找到不能覆盖的最晚日期，二分搜索。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:

    def mincostTickets(self, days: List[int], costs: List[int]) -> int:

        dp = [min(costs)]

        costs = list(zip([1, 7, 30], costs))
        for i in range(1, len(days)):
            now = days[i]
            res = inf
            for d, c in costs:
                idx = bisect_right(days, now - d) - 1
                dpC = dp[idx] if idx >= 0 else 0
                res = min(res, dpC + c)
            dp.append(res)
        return dp[-1]

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('days = [1,4,6,7,8,20], costs = [2,7,15]')
    print('Exception :')
    print('11')
    print('Output :')
    print(str(Solution().mincostTickets([1, 4, 6, 7, 8, 20], [2, 7, 15])))
    print()

    print('Example 2:')
    print('Input : ')
    print('days = [1,2,3,4,5,6,7,8,9,10,30,31], costs = [2,7,15]')
    print('Exception :')
    print('17')
    print('Output :')
    print(
        str(Solution().mincostTickets([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31],
                                      [2, 7, 15])))
    print()

    pass
# @lc main=end