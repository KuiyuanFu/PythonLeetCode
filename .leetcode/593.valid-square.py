# @lc app=leetcode id=593 lang=python3
#
# [593] Valid Square
#
# https://leetcode.com/problems/valid-square/description/
#
# algorithms
# Medium (43.44%)
# Likes:    557
# Dislikes: 660
# Total Accepted:    70.5K
# Total Submissions: 162.1K
# Testcase Example:  '[0,0]\n[1,1]\n[1,0]\n[0,1]'
#
# Given the coordinates of four points in 2D space p1, p2, p3 and p4, return
# true if the four points construct a square.
#
# The coordinate of a point pi is represented as [xi, yi]. The input is not
# given in any order.
#
# A valid square has four equal sides with positive length and four equal
# angles (90-degree angles).
#
#
# Example 1:
#
#
# Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]
# Output: true
#
#
# Example 2:
#
#
# Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,12]
# Output: false
#
#
# Example 3:
#
#
# Input: p1 = [1,0], p2 = [-1,0], p3 = [0,1], p4 = [0,-1]
# Output: true
#
#
#
# Constraints:
#
#
# p1.length == p2.length == p3.length == p4.length == 2
# -10^4 <= xi, yi <= 10^4
#
#
#

# @lc tags=math

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 判断是否是矩形。
# 勾股定理。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int],
                    p4: List[int]) -> bool:
        ps = [p1, p2, p3, p4]
        ps.sort()
        p1, p2, p3, p4 = ps

        def ls(p1, p2):
            x = abs(p1[0] - p2[0])
            y = abs(p1[1] - p2[1])
            return x * x + y * y

        def isRightAngle(a, b, c):
            return a + b == c

        s1, s2, s3, s4 = ls(p1, p2), ls(p1, p3), ls(p4, p2), ls(p4, p3),
        d1, d2 = ls(p3, p2), ls(p1, p4),

        return s1!=0 and s2!=0 and s3!=0 and s4!=0 and \
            s1 == s2 == s3 == s4 and \
            isRightAngle(s1, s2, d1) and \
            isRightAngle(s3, s4, d1) and \
            isRightAngle(s1, s3, d2)

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().validSquare([0, 0], [1, 1], [1, 0], [0, 1])))
    print()

    print('Example 2:')
    print('Input : ')
    print('p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,12]')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().validSquare([0, 0], [1, 1], [1, 0], [0, 12])))
    print()

    print('Example 3:')
    print('Input : ')
    print('p1 = [1,0], p2 = [-1,0], p3 = [0,1], p4 = [0,-1]')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().validSquare([1, 0], [-1, 0], [0, 1], [0, -1])))
    print()
    print(str(Solution().validSquare([0, 0], [5, 0], [5, 4], [0, 4])))
    pass
# @lc main=end