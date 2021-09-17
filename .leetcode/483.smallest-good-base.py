# @lc app=leetcode id=483 lang=python3
#
# [483] Smallest Good Base
#
# https://leetcode.com/problems/smallest-good-base/description/
#
# algorithms
# Hard (37.01%)
# Likes:    229
# Dislikes: 390
# Total Accepted:    15.4K
# Total Submissions: 41.5K
# Testcase Example:  '"13"'
#
# Given an integer n represented as a string, return the smallest good base of
# n.
#
# We call k >= 2 a good base of n, if all digits of n base k are 1's.
#
#
# Example 1:
#
#
# Input: n = "13"
# Output: "3"
# Explanation: 13 base 3 is 111.
#
#
# Example 2:
#
#
# Input: n = "4681"
# Output: "8"
# Explanation: 4681 base 8 is 11111.
#
#
# Example 3:
#
#
# Input: n = "1000000000000000000"
# Output: "999999999999999999"
# Explanation: 1000000000000000000 base 999999999999999999 is 11.
#
#
#
# Constraints:
#
#
# n is an integer in the range [3, 10^18].
# n does not contain any leading zeros.
#
#
#

# @lc tags=math;binary-search

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定数字，求最小的基数，使表示法为全1.
# 表示数位数由低到高依次遍历，每次二分搜索基数。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def smallestGoodBase(self, n: str) -> str:
        n = int(n)

        # 找n二进制位数
        def bn(n):
            r = 0
            while n != 0:
                r += 1
                n >>= 1
            return r

        nbn = bn(n)

        for i in range(nbn, 1, -1):

            l, r = 1, n - 1
            ran = list(range(i))
            while l <= r:
                base = (l + r) // 2

                rp = 0
                t = 1
                for _ in ran:
                    rp += t
                    if rp > n:
                        break
                    t = t * base
                if rp == n:
                    return str(base)
                elif rp > n:
                    r = base - 1
                else:
                    l = base + 1
        return str(n - 1)
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('n = "13"')
    print('Exception :')
    print('"3"')
    print('Output :')
    print(str(Solution().smallestGoodBase("13")))
    print()

    print('Example 2:')
    print('Input : ')
    print('n = "4681"')
    print('Exception :')
    print('"8"')
    print('Output :')
    print(str(Solution().smallestGoodBase("4681")))
    print()

    print('Example 3:')
    print('Input : ')
    print('n = "1000000000000000000"')
    print('Exception :')
    print('"999999999999999999"')
    print('Output :')
    print(str(Solution().smallestGoodBase("1000000000000000000")))
    print()

    pass
# @lc main=end