# @lc app=leetcode id=223 lang=python3
#
# [223] Rectangle Area
#
# https://leetcode.com/problems/rectangle-area/description/
#
# algorithms
# Medium (38.56%)
# Likes:    561
# Dislikes: 890
# Total Accepted:    121.3K
# Total Submissions: 313.9K
# Testcase Example:  '-3\n0\n3\n4\n0\n-1\n9\n2'
#
# Given the coordinates of two rectilinear rectangles in a 2D plane, return the
# total area covered by the two rectangles.
#
# The first rectangle is defined by its bottom-left corner (ax1, ay1) and its
# top-right corner (ax2, ay2).
#
# The second rectangle is defined by its bottom-left corner (bx1, by1) and its
# top-right corner (bx2, by2).
#
#
# Example 1:
#
#
# Input: ax1 = -3, ay1 = 0, ax2 = 3, ay2 = 4, bx1 = 0, by1 = -1, bx2 = 9, by2 =
# 2
# Output: 45
#
#
# Example 2:
#
#
# Input: ax1 = -2, ay1 = -2, ax2 = 2, ay2 = 2, bx1 = -2, by1 = -2, bx2 = 2, by2
# = 2
# Output: 16
#
#
#
# Constraints:
#
#
# -10^4 <= ax1, ay1, ax2, ay2, bx1, by1, bx2, by2 <= 10^4
#
#
#

# @lc tags=math

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定两个矩阵，求所有覆盖的区域面积。
# 通过点，来判断是否有重复区域。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int,
                    by1: int, bx2: int, by2: int) -> int:
        duplArea = 0
        if not (ax1 >= bx2 or ax2 <= bx1 or ay1 >= by2 or ay2 <= by1):
            x1, x2, = max(ax1, bx1), min(ax2, bx2)
            y1, y2 = max(ay1, by1), min(ay2, by2)
            duplArea = (x2 - x1) * (y2 - y1)
        return (ax2 - ax1) * (ay2 - ay1) + (bx2 - bx1) * (by2 - by1) - duplArea


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print(
        'ax1 = -3, ay1 = 0, ax2 = 3, ay2 = 4, bx1 = 0, by1 = -1, bx2 = 9, by2 =2'
    )
    print('Exception :')
    print('45')
    print('Output :')
    print(str(Solution().computeArea(-3, 0, 3, 4, 0, -1, 9, 2)))
    print()

    print('Example 2:')
    print('Input : ')
    print(
        'ax1 = -2, ay1 = -2, ax2 = 2, ay2 = 2, bx1 = -2, by1 = -2, bx2 = 2, by2= 2'
    )
    print('Exception :')
    print('16')
    print('Output :')
    print(str(Solution().computeArea(-2, -2, 2, 2, -2, -2, 2, 2)))
    print()

    pass
# @lc main=end