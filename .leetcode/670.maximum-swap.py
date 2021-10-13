# @lc app=leetcode id=670 lang=python3
#
# [670] Maximum Swap
#
# https://leetcode.com/problems/maximum-swap/description/
#
# algorithms
# Medium (45.87%)
# Likes:    1909
# Dislikes: 111
# Total Accepted:    120.2K
# Total Submissions: 260K
# Testcase Example:  '2736'
#
# You are given an integer num. You can swap two digits at most once to get the
# maximum valued number.
#
# Return the maximum valued number you can get.
#
#
# Example 1:
#
#
# Input: num = 2736
# Output: 7236
# Explanation: Swap the number 2 and the number 7.
#
#
# Example 2:
#
#
# Input: num = 9973
# Output: 9973
# Explanation: No swap.
#
#
#
# Constraints:
#
#
# 0 <= num <= 10^8
#
#
#

# @lc tags=array;math

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 交换数字中的一位，使结果最大。
# 从后先前找每一位之后的最大值，将第一个有比其的值的元素互换。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def maximumSwap(self, num: int) -> int:
        s = str(num)
        buffer = [None] * len(s)
        mc = ('0', len(s))
        for i in range(len(s) - 1, -1, -1):
            c = s[i]
            if c < mc[0]:
                buffer[i] = mc
            elif c > mc[0]:
                mc = (c, i)
        for i, c in enumerate(buffer):
            if c != None:
                t = c[1]
                s = s[:i] + s[t] + s[i + 1:t] + s[i] + s[t + 1:]
                break
        return s
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('num = 2736')
    print('Exception :')
    print('7236')
    print('Output :')
    print(str(Solution().maximumSwap(2736)))
    print()

    print('Example 2:')
    print('Input : ')
    print('num = 9973')
    print('Exception :')
    print('9973')
    print('Output :')
    print(str(Solution().maximumSwap(9973)))
    print()
    print('num = 98368')
    print('Exception :')
    print('98863')
    print('Output :')
    print(str(Solution().maximumSwap(98368)))
    pass
# @lc main=end