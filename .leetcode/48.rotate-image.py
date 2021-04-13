#
# @lc app=leetcode id=48 lang=python3
#
# [48] Rotate Image
#
# https://leetcode.com/problems/rotate-image/description/
#
# algorithms
# Medium (60.46%)
# Likes:    4648
# Dislikes: 331
# Total Accepted:    556.7K
# Total Submissions: 919.2K
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
#
# You are given an n x n 2D matrix representing an image, rotate the image by
# 90 degrees (clockwise).
#
# You have to rotate the image in-place, which means you have to modify the
# input 2D matrix directly. DO NOT allocate another 2D matrix and do the
# rotation.
#
#
# Example 1:
#
#
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[7,4,1],[8,5,2],[9,6,3]]
#
#
# Example 2:
#
#
# Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
# Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
#
#
# Example 3:
#
#
# Input: matrix = [[1]]
# Output: [[1]]
#
#
# Example 4:
#
#
# Input: matrix = [[1,2],[3,4]]
# Output: [[3,1],[4,2]]
#
#
#
# Constraints:
#
#
# matrix.length == n
# matrix[i].length == n
# 1 <= n <= 20
# -1000 <= matrix[i][j] <= 1000
#
#
#
#
#
# @lc idea=start
#
# 原地旋转一个方阵。
# 把旋转看成两次反转。一次上下反转，一次左下右上反转
#
# @lc idea=end

from typing import *
from collections import *


# @lc code=start
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        self.upToDown(matrix)
        self.leftDownToRightUp(matrix)
        return matrix

    def upToDown(self, matrix):
        for i in range(len(matrix)//2):
            matrix[i], matrix[-1-i] = matrix[-1-i], matrix[i]

    def leftDownToRightUp(self, matrix):
        for i in range(0, len(matrix)):
            for j in range(i+1, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
# @lc code=end
if __name__ == '__main__':
    print(Solution().rotate([[1,2,3],[4,5,6],[7,8,9]]))
