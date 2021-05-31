# @lc app=leetcode id=134 lang=python3
#
# [134] Gas Station
#
# https://leetcode.com/problems/gas-station/description/
#
# algorithms
# Medium (41.92%)
# Likes:    3119
# Dislikes: 442
# Total Accepted:    289.5K
# Total Submissions: 690.6K
# Testcase Example:  '[1,2,3,4,5]\n[3,4,5,1,2]'
#
# There are n gas stations along a circular route, where the amount of gas at
# the i^th station is gas[i].
#
# You have a car with an unlimited gas tank and it costs cost[i] of gas to
# travel from the i^th station to its next (i + 1)^th station. You begin the
# journey with an empty tank at one of the gas stations.
#
# Given two integer arrays gas and cost, return the starting gas station's
# index if you can travel around the circuit once in the clockwise direction,
# otherwise return -1. If there exists a solution, it is guaranteed to be
# unique
#
#
# Example 1:
#
#
# Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
# Output: 3
# Explanation:
# Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 +
# 4 = 4
# Travel to station 4. Your tank = 4 - 1 + 5 = 8
# Travel to station 0. Your tank = 8 - 2 + 1 = 7
# Travel to station 1. Your tank = 7 - 3 + 2 = 6
# Travel to station 2. Your tank = 6 - 4 + 3 = 5
# Travel to station 3. The cost is 5. Your gas is just enough to travel back to
# station 3.
# Therefore, return 3 as the starting index.
#
#
# Example 2:
#
#
# Input: gas = [2,3,4], cost = [3,4,3]
# Output: -1
# Explanation:
# You can't start at station 0 or 1, as there is not enough gas to travel to
# the next station.
# Let's start at station 2 and fill up with 4 unit of gas. Your tank = 0 + 4 =
# 4
# Travel to station 0. Your tank = 4 - 3 + 2 = 3
# Travel to station 1. Your tank = 3 - 3 + 3 = 3
# You cannot travel back to station 2, as it requires 4 unit of gas but you
# only have 3.
# Therefore, you can't travel around the circuit once no matter where you
# start.
#
#
#
# Constraints:
#
#
# gas.length == n
# cost.length == n
# 1 <= n <= 10^4
# 0 <= gas[i], cost[i] <= 10^4
#
#
#

# @lc tags=greedy

# @lc imports=start

from imports import *

# @lc imports=end

# @lc idea=start
#
# 环路上有n个气站，气站有一定的气，路程需要消耗气。
# 求，从哪一个气站出发，可以绕一圈。结果唯一。
# 直接求。
# 如果气站的气，够行驶到下一站，那么下一站一定不是起点。
# 起始站点是，累计欠气最多的站的下一站，这样才能累计最多的气，应对这个大欠气。
#
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        g = 0
        m = 1
        index = 0
        for i in range(len(gas)):
            # station remain gas
            gas[i] = gas[i] - cost[i]
            # car remain gas
            g += gas[i]
            # the minimum
            if g < m:
                m = g
                index = i
        # remain gas bigger than 0
        if g >= 0:
            return (index + 1) % len(gas)
        else:
            return -1

        return

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print(str(Solution().canCompleteCircuit([3, 1, 1], [1, 2, 2])))
    print('Example 1:')
    print('Input : ')
    print('gas = [1,2,3,4,5], cost = [3,4,5,1,2]')
    print('Exception :')
    print('3')
    print('Output :')
    print(str(Solution().canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2])))
    print()

    print('Example 2:')
    print('Input : ')
    print('gas = [2,3,4], cost = [3,4,3]')
    print('Exception :')
    print('-1')
    print('Output :')
    print(str(Solution().canCompleteCircuit([2, 3, 4], [3, 4, 3])))
    print()

    pass
# @lc main=end