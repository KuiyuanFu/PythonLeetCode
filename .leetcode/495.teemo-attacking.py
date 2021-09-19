# @lc app=leetcode id=495 lang=python3
#
# [495] Teemo Attacking
#
# https://leetcode.com/problems/teemo-attacking/description/
#
# algorithms
# Easy (56.34%)
# Likes:    129
# Dislikes: 20
# Total Accepted:    83K
# Total Submissions: 147.2K
# Testcase Example:  '[1,4]\n2'
#
# Our hero Teemo is attacking an enemy Ashe with poison attacks! When Teemo
# attacks Ashe, Ashe gets poisoned for a exactly duration seconds. More
# formally, an attack at second t will mean Ashe is poisoned during the
# inclusive time interval [t, t + duration - 1]. If Teemo attacks again before
# the poison effect ends, the timer for it is reset, and the poison effect will
# end duration seconds after the new attack.
#
# You are given a non-decreasing integer array timeSeries, where timeSeries[i]
# denotes that Teemo attacks Ashe at second timeSeries[i], and an integer
# duration.
#
# Return the total number of seconds that Ashe is poisoned.
#
#
# Example 1:
#
#
# Input: timeSeries = [1,4], duration = 2
# Output: 4
# Explanation: Teemo's attacks on Ashe go as follows:
# - At second 1, Teemo attacks, and Ashe is poisoned for seconds 1 and 2.
# - At second 4, Teemo attacks, and Ashe is poisoned for seconds 4 and 5.
# Ashe is poisoned for seconds 1, 2, 4, and 5, which is 4 seconds in total.
#
#
# Example 2:
#
#
# Input: timeSeries = [1,2], duration = 2
# Output: 3
# Explanation: Teemo's attacks on Ashe go as follows:
# - At second 1, Teemo attacks, and Ashe is poisoned for seconds 1 and 2.
# - At second 2 however, Teemo attacks again and resets the poison timer. Ashe
# is poisoned for seconds 2 and 3.
# Ashe is poisoned for seconds 1, 2, and 3, which is 3 seconds in total.
#
#
# Constraints:
#
#
# 1 <= timeSeries.length <= 10^4
# 0 <= timeSeries[i], duration <= 10^7
# timeSeries is sorted in non-decreasing order.
#
#
#

# @lc tags=array

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 分时间下毒，每次毒效果持续一定时间，从新下毒会重置时间。求中毒持续时间。
# 直接遍历即可。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def findPoisonedDuration(self, timeSeries: List[int],
                             duration: int) -> int:
        res = duration
        for i in range(1, len(timeSeries)):
            res += min(duration, timeSeries[i] - timeSeries[i - 1])
        return res

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('timeSeries = [1,4], duration = 2')
    print('Exception :')
    print('4')
    print('Output :')
    print(str(Solution().findPoisonedDuration([1, 4], 2)))
    print()

    print('Example 2:')
    print('Input : ')
    print('timeSeries = [1,2], duration = 2')
    print('Exception :')
    print('3')
    print('Output :')
    print(str(Solution().findPoisonedDuration([1, 2], 2)))
    print()

    pass
# @lc main=end