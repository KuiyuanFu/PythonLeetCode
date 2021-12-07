# @lc app=leetcode id=793 lang=python3
#
# [793] Preimage Size of Factorial Zeroes Function
#
# https://leetcode.com/problems/preimage-size-of-factorial-zeroes-function/description/
#
# algorithms
# Hard (40.84%)
# Likes:    266
# Dislikes: 65
# Total Accepted:    11.1K
# Total Submissions: 26.9K
# Testcase Example:  '0'
#
# Let f(x) be the number of zeroes at the end of x!. Recall that x! = 1 * 2 * 3
# * ... * x and by convention, 0! = 1.
#
#
# For example, f(3) = 0 because 3! = 6 has no zeroes at the end, while f(11) =
# 2 because 11! = 39916800 has two zeroes at the end.
#
#
# Given an integer k, return the number of non-negative integers x have the
# property that f(x) = k.
#
#
# Example 1:
#
#
# Input: k = 0
# Output: 5
# Explanation: 0!, 1!, 2!, 3!, and 4! end with k = 0 zeroes.
#
#
# Example 2:
#
#
# Input: k = 5
# Output: 0
# Explanation: There is no x such that x! ends in k = 5 zeroes.
#
#
# Example 3:
#
#
# Input: k = 3
# Output: 5
#
#
#
# Constraints:
#
#
# 0 <= k <= 10^9
#
#
#

# @lc tags=brainteaser

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 函数为阶乘结尾0的个数，给定函数结果，求有多少个数的结果为这个数。
# 每过5个数就至少遇到一个5，就会增加0，如果遇到25就会增加两个0，
# 所以结果只能是0或者5两个选项。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def preimageSizeFZF(self, k: int) -> int:

        # the zero count in 0-5^0, 0-5^1, 0-5^2,
        counts = [
            0,
            1,
            6,
        ]
        while counts[-1] - len(counts) < k:
            counts.append(counts[-1] * 5 + 1)
        # the increase threshold, the number is the index.
        for i, c in enumerate(counts):
            counts[i] = c - i

        while True:
            if k < 5:
                return 5
            idx = bisect_left(counts, k) - 1
            t = counts[idx] + idx
            if k == t:
                return 5
            elif k < t:
                return 0
            else:
                k = k % t


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('k = 0')
    print('Exception :')
    print('5')
    print('Output :')
    print(str(Solution().preimageSizeFZF(0)))
    print()

    print('Example 2:')
    print('Input : ')
    print('k = 5')
    print('Exception :')
    print('0')
    print('Output :')
    print(str(Solution().preimageSizeFZF(5)))
    print()

    print('Example 3:')
    print('Input : ')
    print('k = 3')
    print('Exception :')
    print('5')
    print('Output :')
    print(str(Solution().preimageSizeFZF(3)))
    print()
    print('Example 3:')
    print('Input : ')
    print('k = 25')
    print('Exception :')
    print('5')
    print('Output :')
    print(str(Solution().preimageSizeFZF(25)))
    print()

    pass
# @lc main=end