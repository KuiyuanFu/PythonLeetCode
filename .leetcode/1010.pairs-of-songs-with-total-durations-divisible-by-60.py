# @lc app=leetcode id=1010 lang=python3
#
# [1010] Pairs of Songs With Total Durations Divisible by 60
#
# https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/description/
#
# algorithms
# Medium (53.06%)
# Likes:    3495
# Dislikes: 136
# Total Accepted:    216K
# Total Submissions: 407K
# Testcase Example:  '[30,20,150,100,40]'
#
# You are given a list of songs where the i^th song has a duration of time[i]
# seconds.
#
# Return the number of pairs of songs for which their total duration in seconds
# is divisible by 60. Formally, we want the number of indices i, j such that i
# < j with (time[i] + time[j]) % 60 == 0.
#
#
# Example 1:
#
#
# Input: time = [30,20,150,100,40]
# Output: 3
# Explanation: Three pairs have a total duration divisible by 60:
# (time[0] = 30, time[2] = 150): total duration 180
# (time[1] = 20, time[3] = 100): total duration 120
# (time[1] = 20, time[4] = 40): total duration 60
#
#
# Example 2:
#
#
# Input: time = [60,60,60]
# Output: 3
# Explanation: All three pairs have a total duration of 120, which is divisible
# by 60.
#
#
#
# Constraints:
#
#
# 1 <= time.length <= 6 * 10^4
# 1 <= time[i] <= 500
#
#
#

# @lc tags=hash-table;math

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 找所有对数，使和可被60整除
# 取模计数，0 30 为特例
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:

    def numPairsDivisibleBy60(self, time: List[int]) -> int:

        counter = Counter(t % 60 for t in time)

        res = sum(counter[k] *
                  counter[60 - k] if 0 < k < 30 and 60 - k in counter else 0
                  for k in counter.keys())
        res += counter[0] * (counter[0] - 1) // 2 if 0 in counter else 0
        res += counter[30] * (counter[30] - 1) // 2 if 30 in counter else 0
        return res
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('time = [30,20,150,100,40]')
    print('Exception :')
    print('3')
    print('Output :')
    print(str(Solution().numPairsDivisibleBy60([30, 20, 150, 100, 40])))
    print()

    print('Example 2:')
    print('Input : ')
    print('time = [60,60,60]')
    print('Exception :')
    print('3')
    print('Output :')
    print(str(Solution().numPairsDivisibleBy60([60, 60, 60])))
    print()

    pass
# @lc main=end