# @lc app=leetcode id=390 lang=python3
#
# [390] Elimination Game
#
# https://leetcode.com/problems/elimination-game/description/
#
# algorithms
# Medium (45.71%)
# Likes:    637
# Dislikes: 448
# Total Accepted:    40.6K
# Total Submissions: 88.8K
# Testcase Example:  '9'
#
# You have a list arr of all integers in the range [1, n] sorted in a strictly
# increasing order. Apply the following algorithm on arr:
#
#
# Starting from left to right, remove the first number and every other number
# afterward until you reach the end of the list.
# Repeat the previous step again, but this time from right to left, remove the
# rightmost number and every other number from the remaining numbers.
# Keep repeating the steps again, alternating left to right and right to left,
# until a single number remains.
#
#
# Given the integer n, return the last number that remains in arr.
#
#
# Example 1:
#
#
# Input: n = 9
# Output: 6
# Explanation:
# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# arr = [2, 4, 6, 8]
# arr = [2, 6]
# arr = [6]
#
#
# Example 2:
#
#
# Input: n = 1
# Output: 1
#
#
#
# Constraints:
#
#
# 1 <= n <= 10^9
#
#
#

# @lc tags=Unknown

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定n，序列为1-n，每次隔一个删除一个，直到剩下一个数字。
# 记录最小的数字，每次距离下一个数字的间隔扩大为二倍，根据剩余数字个数的奇偶，和遍历方向，来确定最小数字是否移动。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def lastRemaining(self, n: int) -> int:
        m = 1
        interval = 1
        f = True
        while n > 1:
            if f or n % 2 == 1:
                m += interval
            interval *= 2
            f = not f
            n //= 2

        return m

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('n = 9')
    print('Exception :')
    print('6')
    print('Output :')
    print(str(Solution().lastRemaining(9)))
    print()

    print('Example 2:')
    print('Input : ')
    print('n = 1')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().lastRemaining(1)))
    print()

    pass
# @lc main=end