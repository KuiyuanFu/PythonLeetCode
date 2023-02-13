# @lc app=leetcode id=1037 lang=python3
#
# [1037] Valid Boomerang
#
# https://leetcode.com/problems/valid-boomerang/description/
#
# algorithms
# Easy (37.22%)
# Likes:    310
# Dislikes: 439
# Total Accepted:    39.4K
# Total Submissions: 105.8K
# Testcase Example:  '[[1,1],[2,3],[3,2]]'
#
# Given an array points where points[i] = [xi, yi] represents a point on the
# X-Y plane, return true if these points are a boomerang.
#
# A boomerang is a set of three points that are all distinct and not in a
# straight line.
#
#
# Example 1:
# Input: points = [[1,1],[2,3],[3,2]]
# Output: true
# Example 2:
# Input: points = [[1,1],[2,2],[3,3]]
# Output: false
#
#
# Constraints:
#
#
# points.length == 3
# points[i].length == 2
# 0 <= xi, yi <= 100
#
#
#

# @lc tags=greedy;sliding-window

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 判断三点是否共线
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:

    def isBoomerang(self, points: List[List[int]]) -> bool:
        x0, y0 = points[0]
        x1, y1 = points[1]
        x2, y2 = points[2]
        s = 0.5 * ((x0 * y1 - x0 * y2) + (x1 * y2 - x1 * y0) +
                   (x2 * y0 - x2 * y1))
        return s != 0
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('points = [[1,1],[2,3],[3,2]]')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().isBoomerang([[1, 1], [2, 3], [3, 2]])))
    print()

    print('Example 2:')
    print('Input : ')
    print('points = [[1,1],[2,2],[3,3]]')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().isBoomerang([[1, 1], [2, 2], [3, 3]])))
    print()
    print('Example 2:')
    print('Input : ')
    print('points = [[1,1],[2,2],[22]]')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().isBoomerang([[1, 1], [2, 2], [2, 2]])))
    print()

    pass
# @lc main=end