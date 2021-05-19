# @lc app=leetcode id=118 lang=python3
#
# [118] Pascal's Triangle
#
# https://leetcode.com/problems/pascals-triangle/description/
#
# algorithms
# Easy (55.73%)
# Likes:    2525
# Dislikes: 132
# Total Accepted:    492.7K
# Total Submissions: 879.1K
# Testcase Example:  '5'
#
# Given an integer numRows, return the first numRows of Pascal's triangle.
#
# In Pascal's triangle, each number is the sum of the two numbers directly
# above it as shown:
#
#
# Example 1:
# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
# Example 2:
# Input: numRows = 1
# Output: [[1]]
#
#
# Constraints:
#
#
# 1 <= numRows <= 30
#
#
#

# @lc tags=array

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 帕斯卡三角，每一个数都是上一层两个数的和，给定层数，求这个三角。
# 直接遍历。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        for n in range(numRows):
            layer = [1] * (n + 1)
            for i in range(1, n):
                layer[i] = result[-1][i - 1] + result[-1][i]
            result.append(layer)
        return result

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('numRows = 5')
    print('Output :')
    print(str(Solution().generate(5)))
    print('Exception :')
    print('[[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]')
    print()

    print('Example 2:')
    print('Input : ')
    print('numRows = 1')
    print('Output :')
    print(str(Solution().generate(1)))
    print('Exception :')
    print('[[1]]')
    print()

    pass
# @lc main=end