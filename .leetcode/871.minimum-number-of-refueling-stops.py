# @lc app=leetcode id=871 lang=python3
#
# [871] Minimum Number of Refueling Stops
#
# https://leetcode.com/problems/minimum-number-of-refueling-stops/description/
#
# algorithms
# Hard (35.61%)
# Likes:    2399
# Dislikes: 47
# Total Accepted:    69.1K
# Total Submissions: 193.9K
# Testcase Example:  '1\n1\n[]'
#
# A car travels from a starting position to a destination which is target miles
# east of the starting position.
#
# There are gas stations along the way. The gas stations are represented as an
# array stations where stations[i] = [positioni, fueli] indicates that the i^th
# gas station is positioni miles east of the starting position and has fueli
# liters of gas.
#
# The car starts with an infinite tank of gas, which initially has startFuel
# liters of fuel in it. It uses one liter of gas per one mile that it drives.
# When the car reaches a gas station, it may stop and refuel, transferring all
# the gas from the station into the car.
#
# Return the minimum number of refueling stops the car must make in order to
# reach its destination. If it cannot reach the destination, return -1.
#
# Note that if the car reaches a gas station with 0 fuel left, the car can
# still refuel there. If the car reaches the destination with 0 fuel left, it
# is still considered to have arrived.
#
#
# Example 1:
#
#
# Input: target = 1, startFuel = 1, stations = []
# Output: 0
# Explanation: We can reach the target without refueling.
#
#
# Example 2:
#
#
# Input: target = 100, startFuel = 1, stations = [[10,100]]
# Output: -1
# Explanation: We can not reach the target (or even the first gas station).
#
#
# Example 3:
#
#
# Input: target = 100, startFuel = 10, stations =
# [[10,60],[20,30],[30,30],[60,40]]
# Output: 2
# Explanation: We start with 10 liters of fuel.
# We drive to position 10, expending 10 liters of fuel.  We refuel from 0
# liters to 60 liters of gas.
# Then, we drive from position 10 to position 60 (expending 50 liters of fuel),
# and refuel from 10 liters to 50 liters of gas.  We then drive to and reach
# the target.
# We made 2 refueling stops along the way, so we return 2.
#
#
#
# Constraints:
#
#
# 1 <= target, startFuel <= 10^9
# 0 <= stations.length <= 500
# 0 <= positioni <= positioni+1 < target
# 1 <= fueli < 10^9
#
#
#

# @lc tags=depth-first-search;graph

# @lc imports=start
from pickletools import read_uint1
import re
from imports import *

# @lc imports=end

# @lc idea=start
#
# 最少加油次数
# 直接动态规划。
# 很慢。
#
# @lc idea=end

# @lc group=array

# @lc rank=10


# @lc code=start
class Solution:
    def minRefuelStops(self, target: int, startFuel: int,
                       stations: List[List[int]]) -> int:
        length = len(stations)
        negativeFuel = -(10**9 * 10**4)
        dp = [startFuel] * (length + 1)
        for p, f in stations:
            for i in range(length + 1):
                if dp[i] < p:
                    dp[i] = negativeFuel
            for i in range(length, 0, -1):
                dp[i] = max(dp[i], dp[i - 1] + f)
        for i in range(length + 1):
            if dp[i] >= target:
                return i
        return -1
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('target = 1, startFuel = 1, stations = []')
    print('Exception :')
    print('0')
    print('Output :')
    print(str(Solution().minRefuelStops(1, 1, [])))
    print()

    print('Example 2:')
    print('Input : ')
    print('target = 100, startFuel = 1, stations = [[10,100]]')
    print('Exception :')
    print('-1')
    print('Output :')
    print(str(Solution().minRefuelStops(100, 1, [[10, 100]])))
    print()

    print('Example 3:')
    print('Input : ')
    print(
        'target = 100, startFuel = 10, stations =[[10,60],[20,30],[30,30],[60,40]]'
    )
    print('Exception :')
    print('2')
    print('Output :')
    print(
        str(Solution().minRefuelStops(
            100, 10, [[10, 60], [20, 30], [30, 30], [60, 40]])))
    print()

    pass
# @lc main=end