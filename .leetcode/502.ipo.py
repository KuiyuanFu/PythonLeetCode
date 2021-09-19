# @lc app=leetcode id=502 lang=python3
#
# [502] IPO
#
# https://leetcode.com/problems/ipo/description/
#
# algorithms
# Hard (42.67%)
# Likes:    623
# Dislikes: 59
# Total Accepted:    26.5K
# Total Submissions: 62K
# Testcase Example:  '2\n0\n[1,2,3]\n[0,1,1]'
#
# Suppose LeetCode will start its IPO soon. In order to sell a good price of
# its shares to Venture Capital, LeetCode would like to work on some projects
# to increase its capital before the IPO. Since it has limited resources, it
# can only finish at most k distinct projects before the IPO. Help LeetCode
# design the best way to maximize its total capital after finishing at most k
# distinct projects.
#
# You are given n projects where the i^th project has a pure profit profits[i]
# and a minimum capital of capital[i] is needed to start it.
#
# Initially, you have w capital. When you finish a project, you will obtain its
# pure profit and the profit will be added to your total capital.
#
# Pick a list of at most k distinct projects from given projects to maximize
# your final capital, and return the final maximized capital.
#
# The answer is guaranteed to fit in a 32-bit signed integer.
#
#
# Example 1:
#
#
# Input: k = 2, w = 0, profits = [1,2,3], capital = [0,1,1]
# Output: 4
# Explanation: Since your initial capital is 0, you can only start the project
# indexed 0.
# After finishing it you will obtain profit 1 and your capital becomes 1.
# With capital 1, you can either start the project indexed 1 or the project
# indexed 2.
# Since you can choose at most 2 projects, you need to finish the project
# indexed 2 to get the maximum capital.
# Therefore, output the final maximized capital, which is 0 + 1 + 3 = 4.
#
#
# Example 2:
#
#
# Input: k = 3, w = 0, profits = [1,2,3], capital = [0,1,2]
# Output: 6
#
#
#
# Constraints:
#
#
# 1 <= k <= 10^5
# 0 <= w <= 10^9
# n == profits.length
# n == capital.length
# 1 <= n <= 10^5
# 0 <= profits[i] <= 10^4
# 0 <= capital[i] <= 10^9
#
#
#

# @lc tags=heap;greedy

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定一系列的项目，每一个项目有成本和纯收益，给定已有资本w，与最多项目数k，求最大剩余资本。
# 这个数量级太大了，不能用dp。
# 贪心，选择剩余项目中，成本小于等于资本的，收益最高的。
# 使用两个堆，第一个堆以成本为序，得到所有当前可以执行的项目。第二个堆在可以执行的项目中找收益最大的。
#
# @lc idea=end

# @lc group=heap;greedy

# @lc rank=10


# @lc code=start
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int],
                             capital: List[int]) -> int:

        ch = list(zip(capital, profits))
        heapify(ch)
        ph = []
        for _ in range(k):
            while ch and ch[0][0] <= w:
                heappush(ph, -heappop(ch)[1])
            if not ph:
                break
            w += -heappop(ph)
        return w


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('k = 2, w = 0, profits = [1,2,3], capital = [0,1,1]')
    print('Exception :')
    print('4')
    print('Output :')
    print(str(Solution().findMaximizedCapital(2, 0, [1, 2, 3], [0, 1, 1])))
    print()

    print('Example 2:')
    print('Input : ')
    print('k = 3, w = 0, profits = [1,2,3], capital = [0,1,2]')
    print('Exception :')
    print('6')
    print('Output :')
    print(str(Solution().findMaximizedCapital(3, 0, [1, 2, 3], [0, 1, 2])))
    print()

    pass
# @lc main=end