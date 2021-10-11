# @lc app=leetcode id=667 lang=python3
#
# [667] Beautiful Arrangement II
#
# https://leetcode.com/problems/beautiful-arrangement-ii/description/
#
# algorithms
# Medium (59.03%)
# Likes:    613
# Dislikes: 925
# Total Accepted:    45.2K
# Total Submissions: 76.4K
# Testcase Example:  '3\n1'
#
# Given two integers n and k, construct a list answer that contains n different
# positive integers ranging from 1 to n and obeys the following
# requirement:
#
#
# Suppose this list is answer = [a1, a2, a3, ... , an], then the list [|a1 -
# a2|, |a2 - a3|, |a3 - a4|, ... , |an-1 - an|] has exactly k distinct
# integers.
#
#
# Return the list answer. If there multiple valid answers, return any of
# them.
#
#
# Example 1:
#
#
# Input: n = 3, k = 1
# Output: [1,2,3]
# Explanation: The [1,2,3] has three different positive integers ranging from 1
# to 3, and the [1,1] has exactly 1 distinct integer: 1
#
#
# Example 2:
#
#
# Input: n = 3, k = 2
# Output: [1,3,2]
# Explanation: The [1,3,2] has three different positive integers ranging from 1
# to 3, and the [2,1] has exactly 2 distinct integers: 1 and 2.
#
#
#
# Constraints:
#
#
# 1 <= k < n <= 10^4
#
#
#

# @lc tags=array

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定数组个数n，有1-n个数，求相邻两者差值种类为k的结果。
# 直接升序，就是一个。首先将最小值，放在首位。
# 此时为最小值，之后每一次，如果剩余数量不为1，那么就插入最大值，反之亦然。
# 这样可以保证每一次插入都会导致一个新的差值。
#
# @lc idea=end
# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        res = [1]
        l, r = 2, n
        while k >= 2:
            if len(res) % 2 == 1:
                res.append(r)
                r -= 1
            else:
                res.append(l)
                l += 1
            k -= 1
        ls = list(range(l, r + 1))
        if len(res) % 2 == 1:
            res += ls
        else:
            res += ls[::-1]
        return res


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('n = 3, k = 1')
    print('Exception :')
    print('[1,2,3]')
    print('Output :')
    print(str(Solution().constructArray(3, 1)))
    print()

    print('Example 2:')
    print('Input : ')
    print('n = 3, k = 2')
    print('Exception :')
    print('[1,3,2]')
    print('Output :')
    print(str(Solution().constructArray(3, 2)))
    print()
    print(str(Solution().constructArray(4, 1)))
    print(str(Solution().constructArray(4, 2)))
    print(str(Solution().constructArray(4, 3)))
    pass
# @lc main=end