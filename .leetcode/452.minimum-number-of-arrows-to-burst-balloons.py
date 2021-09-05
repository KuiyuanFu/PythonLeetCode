# @lc app=leetcode id=452 lang=python3
#
# [452] Minimum Number of Arrows to Burst Balloons
#
# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/description/
#
# algorithms
# Medium (50.51%)
# Likes:    2106
# Dislikes: 74
# Total Accepted:    126.7K
# Total Submissions: 250.9K
# Testcase Example:  '[[10,16],[2,8],[1,6],[7,12]]'
#
# There are some spherical balloons spread in two-dimensional space. For each
# balloon, provided input is the start and end coordinates of the horizontal
# diameter. Since it's horizontal, y-coordinates don't matter, and hence the
# x-coordinates of start and end of the diameter suffice. The start is always
# smaller than the end.
#
# An arrow can be shot up exactly vertically from different points along the
# x-axis. A balloon with xstart and xend bursts by an arrow shot at x if xstart
# ≤ x ≤ xend. There is no limit to the number of arrows that can be shot. An
# arrow once shot keeps traveling up infinitely.
#
# Given an array points where points[i] = [xstart, xend], return the minimum
# number of arrows that must be shot to burst all balloons.
#
#
# Example 1:
#
#
# Input: points = [[10,16],[2,8],[1,6],[7,12]]
# Output: 2
# Explanation: One way is to shoot one arrow for example at x = 6 (bursting the
# balloons [2,8] and [1,6]) and another arrow at x = 11 (bursting the other two
# balloons).
#
#
# Example 2:
#
#
# Input: points = [[1,2],[3,4],[5,6],[7,8]]
# Output: 4
#
#
# Example 3:
#
#
# Input: points = [[1,2],[2,3],[3,4],[4,5]]
# Output: 2
#
#
#
# Constraints:
#
#
# 1 <= points.length <= 10^5
# points[i].length == 2
# -2^31 <= xstart < xend <= 2^31 - 1
#
#
#

# @lc tags=greedy

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 气球水平摆放，箭垂直无线射程，问最少多少个箭全刺破。
# 排序，之后以右侧为基准。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        res = 0
        points.sort()
        pr = points[0][0] - 1
        for l, r in points:
            if l > pr:
                pr = r
                res += 1
            else:
                pr = min(pr, r)
        return res
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('points = [[10,16],[2,8],[1,6],[7,12]]')
    print('Exception :')
    print('2')
    print('Output :')
    print(
        str(Solution().findMinArrowShots([[10, 16], [2, 8], [1, 6], [7, 12]])))
    print()

    print('Example 2:')
    print('Input : ')
    print('points = [[1,2],[3,4],[5,6],[7,8]]')
    print('Exception :')
    print('4')
    print('Output :')
    print(str(Solution().findMinArrowShots([[1, 2], [3, 4], [5, 6], [7, 8]])))
    print()

    print('Example 3:')
    print('Input : ')
    print('points = [[1,2],[2,3],[3,4],[4,5]]')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().findMinArrowShots([[1, 2], [2, 3], [3, 4], [4, 5]])))
    print()

    pass
# @lc main=end