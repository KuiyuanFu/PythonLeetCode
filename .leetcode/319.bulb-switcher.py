# @lc app=leetcode id=319 lang=python3
#
# [319] Bulb Switcher
#
# https://leetcode.com/problems/bulb-switcher/description/
#
# algorithms
# Medium (45.89%)
# Likes:    693
# Dislikes: 1320
# Total Accepted:    96.9K
# Total Submissions: 211.1K
# Testcase Example:  '3'
#
# There are n bulbs that are initially off. You first turn on all the bulbs,
# then you turn off every second bulb.
#
# On the third round, you toggle every third bulb (turning on if it's off or
# turning off if it's on). For the i^th round, you toggle every i bulb. For the
# n^th round, you only toggle the last bulb.
#
# Return the number of bulbs that are on after n rounds.
#
#
# Example 1:
#
#
# Input: n = 3
# Output: 1
# Explanation: At first, the three bulbs are [off, off, off].
# After the first round, the three bulbs are [on, on, on].
# After the second round, the three bulbs are [on, off, on].
# After the third round, the three bulbs are [on, off, off].
# So you should return 1 because there is only one bulb is on.
#
# Example 2:
#
#
# Input: n = 0
# Output: 0
#
#
# Example 3:
#
#
# Input: n = 1
# Output: 1
#
#
#
# Constraints:
#
#
# 0 <= n <= 10^9
#
#
#

# @lc tags=math;brainteaser

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 开关灯泡，一共n轮，第i轮开关所有i的整数倍位置的灯泡，问最后有多少是亮着的。
# 那么第i个灯开着的条件，是一共有奇数个不同的因数，那么只有平方数才可以，因为平方数有一个重复的因数。
#
# @lc idea=end

# @lc group=

# @lc rank=

# @lc code=start
import math


class Solution:
    def bulbSwitch(self, n: int) -> int:
        return int(math.sqrt(n))
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('n = 3')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().bulbSwitch(3)))
    print()

    print('Example 2:')
    print('Input : ')
    print('n = 0')
    print('Exception :')
    print('0')
    print('Output :')
    print(str(Solution().bulbSwitch(0)))
    print()

    print('Example 3:')
    print('Input : ')
    print('n = 1')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().bulbSwitch(1)))
    print()

    pass
# @lc main=end