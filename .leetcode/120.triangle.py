# @lc app=leetcode id=120 lang=python3
#
# [120] Triangle
#
# https://leetcode.com/problems/triangle/description/
#
# algorithms
# Medium (46.94%)
# Likes:    3141
# Dislikes: 324
# Total Accepted:    316.3K
# Total Submissions: 671.9K
# Testcase Example:  '[[2],[3,4],[6,5,7],[4,1,8,3]]'
#
# Given a triangle array, return the minimum path sum from top to bottom.
#
# For each step, you may move to an adjacent number of the row below. More
# formally, if you are on index i on the current row, you may move to either
# index i or index i + 1 on the next row.
#
#
# Example 1:
#
#
# Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
# Output: 11
# Explanation: The triangle looks like:
# ⁠  2
# ⁠ 3 4
# ⁠6 5 7
# 4 1 8 3
# The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined
# above).
#
#
# Example 2:
#
#
# Input: triangle = [[-10]]
# Output: -10
#
#
#
# Constraints:
#
#
# 1 <= triangle.length <= 200
# triangle[0].length == 1
# triangle[i].length == triangle[i - 1].length + 1
# -10^4 <= triangle[i][j] <= 10^4
#
#
#
# Follow up: Could you do this using only O(n) extra space, where n is the
# total number of rows in the triangle?
#

# @lc tags=array;dynamic-programming

# @lc imports=start

from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定一个三角形的数组，求从顶到底的最短路径。
# 直接动态规划，迭代。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for i in reversed(range(len(triangle) - 1)):
            for j in range(len(triangle[i])):
                triangle[i][j] += min(triangle[i + 1][j],
                                      triangle[i + 1][j + 1])
        return triangle[0][0]
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]')
    print('Output :')
    print(str(Solution().minimumTotal([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]])))
    print('Exception :')
    print('11')
    print()

    print('Example 2:')
    print('Input : ')
    print('triangle = [[-10]]')
    print('Output :')
    print(str(Solution().minimumTotal([[-10]])))
    print('Exception :')
    print('-10')
    print()

    pass
# @lc main=end