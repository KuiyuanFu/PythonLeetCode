# @lc app=leetcode id=600 lang=python3
#
# [600] Non-negative Integers without Consecutive Ones
#
# https://leetcode.com/problems/non-negative-integers-without-consecutive-ones/description/
#
# algorithms
# Hard (38.22%)
# Likes:    950
# Dislikes: 103
# Total Accepted:    28.5K
# Total Submissions: 74.4K
# Testcase Example:  '5'
#
# Given a positive integer n, return the number of the integers in the range
# [0, n] whose binary representations do not contain consecutive ones.
#
#
# Example 1:
#
#
# Input: n = 5
# Output: 5
# Explanation:
# Here are the non-negative integers <= 5 with their corresponding binary
# representations:
# 0 : 0
# 1 : 1
# 2 : 10
# 3 : 11
# 4 : 100
# 5 : 101
# Among them, only integer 3 disobeys the rule (two consecutive ones) and the
# other 5 satisfy the rule.
#
#
# Example 2:
#
#
# Input: n = 1
# Output: 2
#
#
# Example 3:
#
#
# Input: n = 2
# Output: 3
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

# @lc tags=dynamic-programming

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定一个整数，求小于其且二进制表示中，不包括连续的1。
# 动态规划，确定每一位为0或1时，接下来会有多少种合理的可能。
# 之后从高位向低位遍历，当遇到单独一个1时，加上此位为0的可能种类。之后认为此位为1，继续遍历。如果需要连续的1，那么将此区域置为合法后，再也达不到最大值了，那么就不需要遍历了，区分结尾为1或0，之后乘上之后的可能性。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def findIntegers(self, n: int) -> int:

        ns = bin(n)[2:]
        # end with 0
        dp = [1, 1, 2]
        while len(dp) <= len(ns) + 1:
            dp.append(dp[-1] + dp[-2])

        res = 1

        l = 0
        length = len(ns)
        while l < length:
            if ns[l] == '0':
                l += 1
                continue

            # idx where not is 1
            r = l + 1
            while r < length and ns[r] == '1':
                r += 1
            # continues 1 length
            q = r - l
            # remain length
            t = length - r

            # q end with 0
            res += dp[q] * dp[t + 1]

            if q != 1:
                # q end with 1
                res += dp[q - 1] * dp[t]
                # n is invalid
                res -= 1
                break

            l = r

        return res
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':

    print('Example 2:')
    print('Input : ')
    print('n = 1')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().findIntegers(1)))
    print()

    print('Example 3:')
    print('Input : ')
    print('n = 2')
    print('Exception :')
    print('3')
    print('Output :')
    print(str(Solution().findIntegers(2)))
    print('Example 1:')
    print('Input : ')
    print('n = 3')
    print('Exception :')
    print('3')
    print('Output :')
    print(str(Solution().findIntegers(3)))
    print()
    print('Example 1:')
    print('Input : ')
    print('n = 5')
    print('Exception :')
    print('5')
    print('Output :')
    print(str(Solution().findIntegers(5)))
    print()
    print('Input : ')
    print('n = 7')
    print('Exception :')
    print('5')
    print('Output :')
    print(str(Solution().findIntegers(7)))
    print('Exception :')
    print('8')
    print('Output :')
    print(str(Solution().findIntegers(11)))
    pass
# @lc main=end