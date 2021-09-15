# @lc app=leetcode id=479 lang=python3
#
# [479] Largest Palindrome Product
#
# https://leetcode.com/problems/largest-palindrome-product/description/
#
# algorithms
# Hard (30.10%)
# Likes:    108
# Dislikes: 1402
# Total Accepted:    18.8K
# Total Submissions: 62.4K
# Testcase Example:  '2'
#
# Given an integer n, return the largest palindromic integer that can be
# represented as the product of two n-digits integers. Since the answer can be
# very large, return it modulo 1337.
#
#
# Example 1:
#
#
# Input: n = 2
# Output: 987
# Explanation: 99 x 91 = 9009, 9009 % 1337 = 987
#
#
# Example 2:
#
#
# Input: n = 1
# Output: 9
#
#
#
# Constraints:
#
#
# 1 <= n <= 8
#
#
#

# @lc tags=Unknown

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 求给定位数的两个数的乘积为回文的最大值。
# 从大到小生成可能的回文数字，之后判断是否合法。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def largestPalindrome(self, n: int) -> int:
        # 3*3
        if n == 1:
            return 9
        # upperbound lowerbound
        ub, lb = 10**n - 1, 10**(n - 1) - 1
        # max mumber
        mm = ub * ub
        # half
        fh = mm // (10**n)
        # flag is palindrom
        pf = False
        # palindrom
        p = 0
        while not pf:
            # str
            s = str(fh)
            p = fh * (10**len(s)) + int(s[::-1])

            for i in range(ub, lb, -1):
                if (p // i) > mm or i * i < p:
                    break
                if p % i == 0:
                    pf = True
                    break

            fh -= 1
        return p % 1337


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('n = 2')
    print('Exception :')
    print('987')
    print('Output :')
    print(str(Solution().largestPalindrome(2)))
    print()

    print('Example 2:')
    print('Input : ')
    print('n = 1')
    print('Exception :')
    print('9')
    print('Output :')
    print(str(Solution().largestPalindrome(1)))
    print()

    pass
# @lc main=end