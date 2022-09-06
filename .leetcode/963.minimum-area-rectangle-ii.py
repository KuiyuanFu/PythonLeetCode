# @lc app=leetcode id=963 lang=python3
#
# [963] Minimum Area Rectangle II
#
# https://leetcode.com/problems/minimum-area-rectangle-ii/description/
#
# algorithms
# Medium (54.67%)
# Likes:    327
# Dislikes: 419
# Total Accepted:    24.1K
# Total Submissions: 44K
# Testcase Example:  '[[1,2],[2,1],[1,0],[0,1]]'
#
# You are given an array of points in the X-Y plane points where points[i] =
# [xi, yi].
#
# Return the minimum area of any rectangle formed from these points, with sides
# not necessarily parallel to the X and Y axes. If there is not any such
# rectangle, return 0.
#
# Answers within 10^-5 of the actual answer will be accepted.
#
#
# Example 1:
#
#
# Input: points = [[1,2],[2,1],[1,0],[0,1]]
# Output: 2.00000
# Explanation: The minimum area rectangle occurs at [1,2],[2,1],[1,0],[0,1],
# with an area of 2.
#
#
# Example 2:
#
#
# Input: points = [[0,1],[2,1],[1,1],[1,0],[2,0]]
# Output: 1.00000
# Explanation: The minimum area rectangle occurs at [1,0],[1,1],[2,1],[2,0],
# with an area of 1.
#
#
# Example 3:
#
#
# Input: points = [[0,3],[1,2],[3,1],[1,3],[2,1]]
# Output: 0
# Explanation: There is no possible rectangle to form from these points.
#
#
#
# Constraints:
#
#
# 1 <= points.length <= 50
# points[i].length == 2
# 0 <= xi, yi <= 4 * 10^4
# All the given points are unique.
#
#
#

# @lc tags=math;binary-search;greedy

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定点数组，求最小矩形面积。
# 直接计算，利用勾股定理确定直角。
# 超时了
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:

    def minAreaFreeRect(self, points: List[List[int]]) -> float:
        res = inf
        points.sort()

        def disSquare(i, j):
            return (i[0] - j[0])**2 + (i[1] - j[1])**2

        def isRightAngle(i, j, k):
            return disSquare(i, j) + disSquare(j, k) == disSquare(i, k)

        for i, j, k, l in combinations(points, 4):
            if isRightAngle(i, j, l) and isRightAngle(
                    i, k, l) and isRightAngle(j, i, k):
                res = min(res, disSquare(i, j)**0.5 * disSquare(i, k)**0.5)

        return res if res != inf else 0

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':

    print()
    print('Example 1:')
    print('Input : ')
    print('points = [[1,2],[2,1],[1,0],[0,1]]')
    print('Exception :')
    print('2.00000')
    print('Output :')
    print(str(Solution().minAreaFreeRect([[1, 2], [2, 1], [1, 0], [0, 1]])))
    print()

    print('Example 2:')
    print('Input : ')
    print('points = [[0,1],[2,1],[1,1],[1,0],[2,0]]')
    print('Exception :')
    print('1.00000')
    print('Output :')
    print(
        str(Solution().minAreaFreeRect([[0, 1], [2, 1], [1, 1], [1, 0], [2,
                                                                         0]])))
    print()

    print('Example 3:')
    print('Input : ')
    print('points = [[0,3],[1,2],[3,1],[1,3],[2,1]]')
    print('Exception :')
    print('0')
    print('Output :')
    print(
        str(Solution().minAreaFreeRect([[0, 3], [1, 2], [3, 1], [1, 3], [2,
                                                                         1]])))
    print()

    print('Example 1:')
    print('Input : ')
    print(
        'points = [[23920,8315],[20157,7676],[28925,28500],[15515,31480],[28500,28925],[7936,22523],[32064,22523],[21885,7820],[20000,7675],[7820,21885],[29765,12480],[22523,7936],[23875,31700],[20000,32325],[32240,18555],[23451,8168],[26996,30147],[30948,14339],[12480,29765],[20444,7683],[8315,23920],[25661,30948],[31165,14780],[18555,32240],[19556,32317],[27035,30120],[28925,11500],[23300,31875],[25661,9052],[31875,16700],[32155,17960],[10235,27520],[26188,9341],[27520,10235],[8520,24485],[28816,28613],[9052,25661],[24485,31480],[9880,27035],[26493,30476],[30476,26493],[25220,31165],[11184,28613],[25800,30875],[22523,32064],[31480,24485],[8168,23451],[11387,28816],[27520,29765],[7676,20157]]'
    )
    print('Exception :')
    print('10944600.00000')
    print('Output :')
    print(
        str(Solution().minAreaFreeRect([[23920, 8315], [20157, 7676],
                                        [28925, 28500], [15515, 31480],
                                        [28500, 28925], [7936, 22523],
                                        [32064, 22523], [21885, 7820],
                                        [20000, 7675], [7820, 21885],
                                        [29765, 12480], [22523, 7936],
                                        [23875, 31700], [20000, 32325],
                                        [32240, 18555], [23451, 8168],
                                        [26996, 30147], [30948, 14339],
                                        [12480, 29765], [20444, 7683],
                                        [8315, 23920], [25661, 30948],
                                        [31165, 14780], [18555, 32240],
                                        [19556, 32317], [27035, 30120],
                                        [28925, 11500], [23300, 31875],
                                        [25661, 9052], [31875, 16700],
                                        [32155, 17960], [10235, 27520],
                                        [26188, 9341], [27520, 10235],
                                        [8520, 24485], [28816, 28613],
                                        [9052, 25661], [24485, 31480],
                                        [9880, 27035], [26493, 30476],
                                        [30476, 26493], [25220, 31165],
                                        [11184, 28613], [25800, 30875],
                                        [22523, 32064], [31480, 24485],
                                        [8168, 23451], [11387, 28816],
                                        [27520, 29765], [7676, 20157]])))

    pass
# @lc main=end