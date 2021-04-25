# @lc app=leetcode id=89 lang=python3
#
# [89] Gray Code
#
# https://leetcode.com/problems/gray-code/description/
#
# algorithms
# Medium (50.75%)
# Likes:    830
# Dislikes: 1802
# Total Accepted:    180K
# Total Submissions: 354.4K
# Testcase Example:  '2'
#
# The gray code is a binary numeral system where two successive values differ
# in only one bit.
#
# Given an integer n representing the total number of bits in the code, return
# any sequence of gray code.
#
# A gray code sequence must begin with 0.
#
#
# Example 1:
#
#
# Input: n = 2
# Output: [0,1,3,2]
# Explanation:
# 00 - 0
# 01 - 1
# 11 - 3
# 10 - 2
# [0,2,3,1] is also a valid gray code sequence.
# 00 - 0
# 10 - 2
# 11 - 3
# 01 - 1
#
#
# Example 2:
#
#
# Input: n = 1
# Output: [0,1]
#
#
#
# Constraints:
#
#
# 1 <= n <= 16
#
#
#

# @lc tags=backtracking

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 格雷码，相邻的两个编码只差一位。给定n表示位数，返回一个合法的格雷码序列
# 就是找规律，每次改变一个位。每一位第一次抵达时，标志位置为True，添加到结果中。之后从新迭代，直到第二次抵达这一位，此时跳过，改变更高位。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def grayCode(self, n: int) -> List[int]:
        now = 0
        result = [0]
        flags = [False] * n
        i = 0
        while i != n:
            flags[i] = not flags[i]
            if flags[i]:
                now = now ^( 1 << i)
                result.append(now)
                i = 0
            else:
                i += 1
        return result
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('n = 2')
    print('Output :')
    print(str(Solution().grayCode(2)))
    print('Exception :')
    print('[0,1,3,2]')
    print()

    print('Example 2:')
    print('Input : ')
    print('n = 1')
    print('Output :')
    print(str(Solution().grayCode(1)))
    print('Exception :')
    print('[0,1]')
    print()

    pass
# @lc main=end