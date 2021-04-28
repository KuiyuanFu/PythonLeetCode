# @lc app=leetcode id=59 lang=python3
#
# [59] Spiral Matrix II
#
# https://leetcode.com/problems/spiral-matrix-ii/description/
#
# algorithms
# Medium (58.18%)
# Likes:    1613
# Dislikes: 129
# Total Accepted:    248.6K
# Total Submissions: 426.9K
# Testcase Example:  '3'
#
# Given a positive integer n, generate an n x n matrix filled with elements
# from 1 to n^2 in spiral order.
#
#
# Example 1:
#
#
# Input: n = 3
# Output: [[1,2,3],[8,9,4],[7,6,5]]
#
#
# Example 2:
#
#
# Input: n = 1
# Output: [[1]]
#
#
#
# Constraints:
#
#
# 1 <= n <= 20
#
#
#
#
#

# @lc tags=array

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 求大小为n的方阵，其中元素以螺旋方式排列。
# 从中心元素到四周元素，从大到小，每次右旋之后增加新的一行。
#
# @lc idea=end

# @lc group=array

# @lc rank=10


# @lc code=start
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:

        number = n * n
        matrix = [[number]]
        while number != 1:
            length = len(matrix)
            l = [list(range(
                number - length,
                number,
            ))]
            matrix = [list(l) for l in (zip(*matrix[::-1]))]
            matrix = l + matrix
            number = number - length

        return matrix


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('n = 3')
    print('Output :')
    print(str(Solution().generateMatrix(3)))
    print('Exception :')
    print('[[1,2,3],[8,9,4],[7,6,5]]')
    print()

    print('Example 2:')
    print('Input : ')
    print('n = 1')
    print('Output :')
    print(str(Solution().generateMatrix(1)))
    print('Exception :')
    print('[[1]]')
    print()

    pass
# @lc main=end