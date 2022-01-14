# @lc app=leetcode id=812 lang=python3
#
# [812] Largest Triangle Area
#
# https://leetcode.com/problems/largest-triangle-area/description/
#
# algorithms
# Easy (59.45%)
# Likes:    301
# Dislikes: 1266
# Total Accepted:    30.5K
# Total Submissions: 51.3K
# Testcase Example:  '[[0,0],[0,1],[1,0],[0,2],[2,0]]'
#
# Given an array of points on the X-Y plane points where points[i] = [xi, yi],
# return the area of the largest triangle that can be formed by any three
# different points. Answers within 10^-5 of the actual answer will be
# accepted.
#
#
# Example 1:
#
#
# Input: points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
# Output: 2.00000
# Explanation: The five points are shown in the above figure. The red triangle
# is the largest.
#
#
# Example 2:
#
#
# Input: points = [[1,0],[0,0],[0,1]]
# Output: 0.50000
#
#
#
# Constraints:
#
#
# 3 <= points.length <= 50
# -50 <= xi, yi <= 50
# All the given points are unique.
#
#
#

# @lc tags=Unknown

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 求最大的三角形面积。
# 海伦公式。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        n = len(points)

        def dist(p1, p2):
            return sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

        res = 0
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    p1, p2, p3 = points[i], points[j], points[k],
                    a, b, c = dist(p1, p2), dist(p2, p3), dist(p3, p1)
                    p = (a + b + c) / 2
                    area = sqrt(max(0, p * (p - a) * (p - b) * (p - c)))
                    res = max(res, area)
        return res

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('points = [[0,0],[0,1],[1,0],[0,2],[2,0]]')
    print('Exception :')
    print('2.00000')
    print('Output :')
    print(
        str(Solution().largestTriangleArea([[0, 0], [0, 1], [1, 0], [0, 2],
                                            [2, 0]])))
    print()

    print('Example 2:')
    print('Input : ')
    print('points = [[1,0],[0,0],[0,1]]')
    print('Exception :')
    print('0.50000')
    print('Output :')
    print(str(Solution().largestTriangleArea([[1, 0], [0, 0], [0, 1]])))
    print()
    print('Example 2:')
    print('Input : ')
    print(
        'points = [[-35,19],[40,19],[27,-20],[35,-3],[44,20],[22,-21],[35,33],[-19,42],[11,47],[11,37]]'
    )
    print('Exception :')
    print('1799.00000')
    print('Output :')
    print(
        str(Solution().largestTriangleArea([[-35, 19], [40, 19], [27, -20],
                                            [35, -3], [44, 20], [22, -21],
                                            [35, 33], [-19, 42], [11, 47],
                                            [11, 37]])))
    print()

    pass
# @lc main=end