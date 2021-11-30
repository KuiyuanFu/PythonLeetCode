# @lc app=leetcode id=787 lang=python3
#
# [787] Cheapest Flights Within K Stops
#
# https://leetcode.com/problems/cheapest-flights-within-k-stops/description/
#
# algorithms
# Medium (37.30%)
# Likes:    4123
# Dislikes: 167
# Total Accepted:    194.9K
# Total Submissions: 532K
# Testcase Example:  '3\n[[0,1,100],[1,2,100],[0,2,500]]\n0\n2\n1'
#
# There are n cities connected by some number of flights. You are given an
# array flights where flights[i] = [fromi, toi, pricei] indicates that there is
# a flight from city fromi to city toi with cost pricei.
#
# You are also given three integers src, dst, and k, return the cheapest price
# from src to dst with at most k stops. If there is no such route, return
# -1.
#
#
# Example 1:
#
#
# Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k
# = 1
# Output: 200
# Explanation: The graph is shown.
# The cheapest price from city 0 to city 2 with at most 1 stop costs 200, as
# marked red in the picture.
#
#
# Example 2:
#
#
# Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k
# = 0
# Output: 500
# Explanation: The graph is shown.
# The cheapest price from city 0 to city 2 with at most 0 stop costs 500, as
# marked blue in the picture.
#
#
#
# Constraints:
#
#
# 1 <= n <= 100
# 0 <= flights.length <= (n * (n - 1) / 2)
# flights[i].length == 3
# 0 <= fromi, toi < n
# fromi != toi
# 1 <= pricei <= 10^4
# There will not be any multiple flights between two cities.
# 0 <= src, dst, k < n
# src != dst
#
#
#

# @lc tags=breadth-first-search

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 城市间在指定最大跳转次数下，最便宜的路线。
# 记录每个结点的价格与经停次数。
# 以价格排序。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int,
                          dst: int, k: int) -> int:
        timess = [n for _ in range(n)]
        fs = [[] for _ in range(n)]
        for f, t, p in flights:
            fs[f].append((t, p))

        heap = [(0, -1, src)]
        while heap:
            cost, times, src = heappop(heap)

            # times is bigger than before and the cost is higher.
            if times >= timess[src]:
                continue
            else:
                timess[src] = times

            if src == dst:
                return cost
            if times == k:
                continue
            times += 1
            for t, p in fs[src]:
                heappush(heap, (cost + p, times, t))
        return -1

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print(
        'n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k= 1'
    )
    print('Exception :')
    print('200')
    print('Output :')
    print(
        str(Solution().findCheapestPrice(
            3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 1)))
    print()

    print('Example 2:')
    print('Input : ')
    print(
        'n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k= 0'
    )
    print('Exception :')
    print('500')
    print('Output :')
    print(
        str(Solution().findCheapestPrice(
            3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 0)))
    print()

    pass
# @lc main=end