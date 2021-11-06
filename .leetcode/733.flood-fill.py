# @lc app=leetcode id=733 lang=python3
#
# [733] Flood Fill
#
# https://leetcode.com/problems/flood-fill/description/
#
# algorithms
# Easy (56.41%)
# Likes:    2867
# Dislikes: 304
# Total Accepted:    295.8K
# Total Submissions: 520.1K
# Testcase Example:  '[[1,1,1],[1,1,0],[1,0,1]]\n1\n1\n2'
#
# An image is represented by an m x n integer grid image where image[i][j]
# represents the pixel value of the image.
#
# You are also given three integers sr, sc, and newColor. You should perform a
# flood fill on the image starting from the pixel image[sr][sc].
#
# To perform a flood fill, consider the starting pixel, plus any pixels
# connected 4-directionally to the starting pixel of the same color as the
# starting pixel, plus any pixels connected 4-directionally to those pixels
# (also with the same color), and so on. Replace the color of all of the
# aforementioned pixels with newColor.
#
# Return the modified image after performing the flood fill.
#
#
# Example 1:
#
#
# Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, newColor = 2
# Output: [[2,2,2],[2,2,0],[2,0,1]]
# Explanation: From the center of the image with position (sr, sc) = (1, 1)
# (i.e., the red pixel), all pixels connected by a path of the same color as
# the starting pixel (i.e., the blue pixels) are colored with the new color.
# Note the bottom corner is not colored 2, because it is not 4-directionally
# connected to the starting pixel.
#
#
# Example 2:
#
#
# Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, newColor = 2
# Output: [[2,2,2],[2,2,2]]
#
#
#
# Constraints:
#
#
# m == image.length
# n == image[i].length
# 1 <= m, n <= 50
# 0 <= image[i][j], newColor < 2^16
# 0 <= sr < m
# 0 <= sc < n
#
#
#

# @lc tags=depth-first-search

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 替换数值。
# 栈。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int,
                  newColor: int) -> List[List[int]]:
        oldColor = image[sr][sc]
        rows, cols = len(image), len(image[0])
        if oldColor != newColor:

            direcs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            s = [(sr, sc)]
            while s:
                i, j = s.pop()
                if 0 <= i < rows and 0 <= j < cols and image[i][j] == oldColor:
                    image[i][j] = newColor
                    for oi, oj in direcs:
                        s.append((i + oi, j + oj))

        return image
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, newColor = 2')
    print('Exception :')
    print('[[2,2,2],[2,2,0],[2,0,1]]')
    print('Output :')
    print(str(Solution().floodFill([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1,
                                   2)))
    print()

    print('Example 2:')
    print('Input : ')
    print('image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, newColor = 2')
    print('Exception :')
    print('[[2,2,2],[2,2,2]]')
    print('Output :')
    print(str(Solution().floodFill([[0, 0, 0], [0, 0, 0]], 0, 0, 2)))
    print()

    pass
# @lc main=end