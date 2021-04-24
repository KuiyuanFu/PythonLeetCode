# @lc app=leetcode id=85 lang=python3
#
# [85] Maximal Rectangle
#
# https://leetcode.com/problems/maximal-rectangle/description/
#
# algorithms
# Hard (39.77%)
# Likes:    4150
# Dislikes: 88
# Total Accepted:    225.3K
# Total Submissions: 566.2K
# Testcase Example:  '[["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]'
#
# Given a rows x cols binary matrix filled with 0's and 1's, find the largest
# rectangle containing only 1's and return its area.
#
#
# Example 1:
#
#
# Input: matrix =
# [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
# Output: 6
# Explanation: The maximal rectangle is shown in the above picture.
#
#
# Example 2:
#
#
# Input: matrix = []
# Output: 0
#
#
# Example 3:
#
#
# Input: matrix = [["0"]]
# Output: 0
#
#
# Example 4:
#
#
# Input: matrix = [["1"]]
# Output: 1
#
#
# Example 5:
#
#
# Input: matrix = [["0","0"]]
# Output: 0
#
#
#
# Constraints:
#
#
# rows == matrix.length
# cols == matrix[i].length
# 0 <= row, cols <= 200
# matrix[i][j] is '0' or '1'.
#
#
#

# @lc tags=array;hash-table;dynamic-programming;stack

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定一个二维数组，元素为0或1，求全为1的最大矩形的面积。
# 这道题可以使用上一题的解题思路，即计算以一行为底，高度为全为一的高度的直方图，计算n次即可。
# 现在使用一种动态规划的方法。
# 使用三个数组，长度都为列长，第一个为 heights ，即以当前行为底，直方图的每个值的高度，可以通过上一行的高度，和当前行的值确定。
# 第二个为 left ，用来保存维持当前高元素度可以达到的最左侧，计算方式为，当前行，从此元素左侧全为1的长度，和上一列维持高度的左侧长度的较右侧的值。
# 第三个为 right，维持高度的最右侧，类似上一个数组。
# 那么以当前元素高度为矩阵的高的矩阵面积，就是 (right - left +1 ) * height。
#
# @lc idea=end

# @lc group=dynamic-programming

# @lc rank=10


# @lc code=start
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        rows = len(matrix)
        cols = len(matrix[0])

        heights = [0] * cols
        lefts = [0] * cols
        rights = [cols - 1] * cols

        result = 0

        for i in range(rows):
            l = 0
            r = cols - 1
            for j in range(cols):
                if matrix[i][j] == '1':
                    heights[j] += 1
                else:
                    heights[j] = 0

            for j in range(cols):
                if matrix[i][j] == '1':
                    lefts[j] = max(lefts[j], l)
                else:
                    l = j + 1
                    lefts[j] = 0

            for j in range(cols)[::-1]:
                if matrix[i][j] == '1':
                    rights[j] = min(rights[j], r)
                else:
                    r = j - 1
                    rights[j] = cols - 1

            for j in range(cols):
                if matrix[i][j] == '1':
                    area = (rights[j] - lefts[j] + 1) * heights[j]
                    result = max(area, result)
        return result


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print(str(Solution().maximalRectangle([["0", "1"]])))

    print('Example 1:')
    print('Input : ')
    print(
        'matrix =[["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]'
    )
    print('Output :')
    print(
        str(Solution().maximalRectangle([["1", "0", "1", "0", "0"],
                                         ["1", "0", "1", "1", "1"],
                                         ["1", "1", "1", "1", "1"],
                                         ["1", "0", "0", "1", "0"]])))
    print('Exception :')
    print('6')
    print()

    print('Example 2:')
    print('Input : ')
    print('matrix = []')
    print('Output :')
    print(str(Solution().maximalRectangle([])))
    print('Exception :')
    print('0')
    print()

    print('Example 3:')
    print('Input : ')
    print('matrix = [["0"]]')
    print('Output :')
    print(str(Solution().maximalRectangle([["0"]])))
    print('Exception :')
    print('0')
    print()

    print('Example 4:')
    print('Input : ')
    print('matrix = [["1"]]')
    print('Output :')
    print(str(Solution().maximalRectangle([["1"]])))
    print('Exception :')
    print('1')
    print()

    print('Example 5:')
    print('Input : ')
    print('matrix = [["0","0"]]')
    print('Output :')
    print(str(Solution().maximalRectangle([["0", "0"]])))
    print('Exception :')
    print('0')
    print()

    pass
# @lc main=end