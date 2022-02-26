# @lc app=leetcode id=832 lang=python3
#
# [832] Flipping an Image
#
# https://leetcode.com/problems/flipping-an-image/description/
#
# algorithms
# Easy (79.46%)
# Likes:    1954
# Dislikes: 197
# Total Accepted:    282.7K
# Total Submissions: 355.7K
# Testcase Example:  '[[1,1,0],[1,0,1],[0,0,0]]'
#
# Given an n x n binary matrix image, flip the image horizontally, then invert
# it, and return the resulting image.
#
# To flip an image horizontally means that each row of the image is
# reversed.
#
#
# For example, flipping [1,1,0] horizontally results in [0,1,1].
#
#
# To invert an image means that each 0 is replaced by 1, and each 1 is replaced
# by 0.
#
#
# For example, inverting [0,1,1] results in [1,0,0].
#
#
#
# Example 1:
#
#
# Input: image = [[1,1,0],[1,0,1],[0,0,0]]
# Output: [[1,0,0],[0,1,0],[1,1,1]]
# Explanation: First reverse each row: [[0,1,1],[1,0,1],[0,0,0]].
# Then, invert the image: [[1,0,0],[0,1,0],[1,1,1]]
#
#
# Example 2:
#
#
# Input: image = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
# Output: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
# Explanation: First reverse each row:
# [[0,0,1,1],[1,0,0,1],[1,1,1,0],[0,1,0,1]].
# Then invert the image: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
#
#
#
# Constraints:
#
#
# n == image.length
# n == image[i].length
# 1 <= n <= 20
# images[i][j] is either 0 or 1.
#
#
#

# @lc tags=tree

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 翻转二维数组。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        n = len(image)
        for i, j in product(range(n), range((n + 1) // 2)):
            image[i][j], image[i][-1 -
                                  j] = 1 - image[i][-1 - j], 1 - image[i][j]
        return image

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('image = [[1,1,0],[1,0,1],[0,0,0]]')
    print('Exception :')
    print('[[1,0,0],[0,1,0],[1,1,1]]')
    print('Output :')
    print(str(Solution().flipAndInvertImage([[1, 1, 0], [1, 0, 1], [0, 0,
                                                                    0]])))
    print()

    print('Example 2:')
    print('Input : ')
    print('image = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]')
    print('Exception :')
    print('[[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]')
    print('Output :')
    print(
        str(Solution().flipAndInvertImage([[1, 1, 0, 0], [1, 0, 0, 1],
                                           [0, 1, 1, 1], [1, 0, 1, 0]])))
    print()

    pass
# @lc main=end