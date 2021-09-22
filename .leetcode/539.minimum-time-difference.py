# @lc app=leetcode id=539 lang=python3
#
# [539] Minimum Time Difference
#
# https://leetcode.com/problems/minimum-time-difference/description/
#
# algorithms
# Medium (52.74%)
# Likes:    765
# Dislikes: 180
# Total Accepted:    66.7K
# Total Submissions: 126.2K
# Testcase Example:  '["23:59","00:00"]'
#
# Given a list of 24-hour clock time points in "HH:MM" format, return the
# minimum minutes difference between any two time-points in the list.
#
# Example 1:
# Input: timePoints = ["23:59","00:00"]
# Output: 1
# Example 2:
# Input: timePoints = ["00:00","23:59","00:00"]
# Output: 0
#
#
# Constraints:
#
#
# 2 <= timePoints <= 2 * 10^4
# timePoints[i] is in the format "HH:MM".
#
#
#

# @lc tags=string

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 求24小时循环的时间最小分钟差。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        def sToTime(s: str):
            ss = s.split(':')
            return int(ss[0]) * 60 + int(ss[1])

        tis = [sToTime(t) for t in timePoints]
        tis.sort()
        res = 24 * 60
        for i in range(len(tis) - 1):
            res = min(res, tis[i + 1] - tis[i])
        res = min(res, 24 * 60 + tis[0] - tis[-1])
        return res

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('timePoints = ["23:59","00:00"]')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().findMinDifference(["23:59", "00:00"])))
    print()

    print('Example 2:')
    print('Input : ')
    print('timePoints = ["00:00","23:59","00:00"]')
    print('Exception :')
    print('0')
    print('Output :')
    print(str(Solution().findMinDifference(["00:00", "23:59", "00:00"])))
    print()

    pass
# @lc main=end