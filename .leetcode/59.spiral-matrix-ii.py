#
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
# @lc idea=start
#
# 求大小为n的方阵，其中元素以螺旋方式排列。
# 由内到外，每次右旋之后增加新的一行。dd
#
# @lc idea=end

from typing import *
from collections import *


# @lc code=start
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:

        number = n * n
        matrix = [[number]]
        while number != 1:
            length = len(matrix)
            l =  [list(range(number- length, number , ))] 
            matrix = [list(l) for l in (zip(*matrix[::-1]))]
            matrix = l + matrix
            number = number - length

        return matrix


# @lc code=end
if __name__ == '__main__':
    # print(Solution().generateMatrix(1))
    # print(Solution().generateMatrix(2))
    print(Solution().generateMatrix(3))
    print(Solution().generateMatrix(4))
    print(Solution().generateMatrix(5))
