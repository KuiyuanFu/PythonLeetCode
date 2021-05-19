# @lc app=leetcode id=119 lang=python3
#
# [119] Pascal's Triangle II
#
# https://leetcode.com/problems/pascals-triangle-ii/description/
#
# algorithms
# Easy (52.67%)
# Likes:    1355
# Dislikes: 222
# Total Accepted:    373.6K
# Total Submissions: 707K
# Testcase Example:  '3'
#
# Given an integer rowIndex, return the rowIndex^th (0-indexed) row of the
# Pascal's triangle.
#
# In Pascal's triangle, each number is the sum of the two numbers directly
# above it as shown:
#
#
# Example 1:
# Input: rowIndex = 3
# Output: [1,3,3,1]
# Example 2:
# Input: rowIndex = 0
# Output: [1]
# Example 3:
# Input: rowIndex = 1
# Output: [1,1]
#
#
# Constraints:
#
#
# 0 <= rowIndex <= 33
#
#
#
# Follow up: Could you optimize your algorithm to use only O(rowIndex) extra
# space?
#
#

# @lc tags=array

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 帕斯卡三角，求给定的行。
# 直接迭代就行。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:

        pre = []
        for n in range(rowIndex + 1):
            layer = [1] * (n + 1)
            for i in range(1, n):
                layer[i] = pre[i - 1] + pre[i]
            pre = layer
        return layer

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('rowIndex = 3')
    print('Output :')
    print(str(Solution().getRow(3)))
    print('Exception :')
    print('[1,3,3,1]')
    print()

    print('Example 2:')
    print('Input : ')
    print('rowIndex = 0')
    print('Output :')
    print(str(Solution().getRow(0)))
    print('Exception :')
    print('[1]')
    print()

    print('Example 3:')
    print('Input : ')
    print('rowIndex = 1')
    print('Output :')
    print(str(Solution().getRow(1)))
    print('Exception :')
    print('[1,1]')
    print()

    pass
# @lc main=end