# @lc app=leetcode id=780 lang=python3
#
# [780] Reaching Points
#
# https://leetcode.com/problems/reaching-points/description/
#
# algorithms
# Hard (30.64%)
# Likes:    860
# Dislikes: 140
# Total Accepted:    36.3K
# Total Submissions: 117.5K
# Testcase Example:  '1\n1\n3\n5'
#
# Given four integers sx, sy, tx, and ty, return true if it is possible to
# convert the point (sx, sy) to the point (tx, ty) through some operations, or
# false otherwise.
#
# The allowed operation on some point (x, y) is to convert it to either (x, x +
# y) or (x + y, y).
#
#
# Example 1:
#
#
# Input: sx = 1, sy = 1, tx = 3, ty = 5
# Output: true
# Explanation:
# One series of moves that transforms the starting point to the target is:
# (1, 1) -> (1, 2)
# (1, 2) -> (3, 2)
# (3, 2) -> (3, 5)
#
#
# Example 2:
#
#
# Input: sx = 1, sy = 1, tx = 2, ty = 2
# Output: false
#
#
# Example 3:
#
#
# Input: sx = 1, sy = 1, tx = 1, ty = 1
# Output: true
#
#
#
# Constraints:
#
#
# 1 <= sx, sy, tx, ty <= 10^9
#
#
#

# @lc tags=array

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 判断是否可以将(x,y)转换到指定点，可以进行转换，为(x+y,y)或(x,x+y)。
# 反向计算。
#
# @lc idea=end

# @lc group=math

# @lc rank=10


# @lc code=start
class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        while sx < tx and sy < ty:
            tx, ty = tx % ty, ty % tx
        return sx == tx and sy <= ty and (ty - sy) % sx == 0 or \
               sy == ty and sx <= tx and (tx - sx) % sy == 0
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('sx = 1, sy = 1, tx = 3, ty = 5')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().reachingPoints(1, 1, 3, 5)))
    print()

    print('Example 2:')
    print('Input : ')
    print('sx = 1, sy = 1, tx = 2, ty = 2')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().reachingPoints(1, 1, 2, 2)))
    print()

    print('Example 3:')
    print('Input : ')
    print('sx = 1, sy = 1, tx = 1, ty = 1')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().reachingPoints(1, 1, 1, 1)))
    print()

    pass
# @lc main=end