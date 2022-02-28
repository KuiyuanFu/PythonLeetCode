# @lc app=leetcode id=836 lang=python3
#
# [836] Rectangle Overlap
#
# https://leetcode.com/problems/rectangle-overlap/description/
#
# algorithms
# Easy (43.15%)
# Likes:    1342
# Dislikes: 375
# Total Accepted:    97.2K
# Total Submissions: 225.4K
# Testcase Example:  '[0,0,2,2]\n[1,1,3,3]'
#
# An axis-aligned rectangle is represented as a list [x1, y1, x2, y2], where
# (x1, y1) is the coordinate of its bottom-left corner, and (x2, y2) is the
# coordinate of its top-right corner. Its top and bottom edges are parallel to
# the X-axis, and its left and right edges are parallel to the Y-axis.
#
# Two rectangles overlap if the area of their intersection is positive. To be
# clear, two rectangles that only touch at the corner or edges do not overlap.
#
# Given two axis-aligned rectangles rec1 and rec2, return true if they overlap,
# otherwise return false.
#
#
# Example 1:
# Input: rec1 = [0,0,2,2], rec2 = [1,1,3,3]
# Output: true
# Example 2:
# Input: rec1 = [0,0,1,1], rec2 = [1,0,2,1]
# Output: false
# Example 3:
# Input: rec1 = [0,0,1,1], rec2 = [2,2,3,3]
# Output: false
#
#
# Constraints:
#
#
# rect1.length == 4
# rect2.length == 4
# -10^9 <= rec1[i], rec2[i] <= 10^9
# rec1 and rec2 represent a valid rectangle with a non-zero area.
#
#
#

# @lc tags=dynamic-programming;heap

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 判断两个正方形是否重叠。
# 判断边是否不重合。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        l1, b1, r1, u1 = rec1
        l2, b2, r2, u2 = rec2
        if (l1 >= r2 or l2 >= r1) or (b1 >= u2 or b2 >= u1):
            return False
        return True

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('rec1 = [0,0,2,2], rec2 = [1,1,3,3]')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().isRectangleOverlap([0, 0, 2, 2], [1, 1, 3, 3])))
    print()

    print('Example 2:')
    print('Input : ')
    print('rec1 = [0,0,1,1], rec2 = [1,0,2,1]')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().isRectangleOverlap([0, 0, 1, 1], [1, 0, 2, 1])))
    print()

    print('Example 3:')
    print('Input : ')
    print('rec1 = [0,0,1,1], rec2 = [2,2,3,3]')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().isRectangleOverlap([0, 0, 1, 1], [2, 2, 3, 3])))
    print()
    print('Example 3:')
    print('Input : ')
    print('[7, 8, 13, 15], [10, 8, 12, 20]')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().isRectangleOverlap([7, 8, 13, 15], [10, 8, 12, 20])))
    print()

    pass
# @lc main=end