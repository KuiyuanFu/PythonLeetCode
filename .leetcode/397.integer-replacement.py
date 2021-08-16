# @lc app=leetcode id=397 lang=python3
#
# [397] Integer Replacement
#
# https://leetcode.com/problems/integer-replacement/description/
#
# algorithms
# Medium (33.79%)
# Likes:    612
# Dislikes: 381
# Total Accepted:    69.9K
# Total Submissions: 206.3K
# Testcase Example:  '8'
#
# Given a positive integer n, you can apply one of the following
# operations:
#
#
# If n is even, replace n with n / 2.
# If n is odd, replace n with either n + 1 or n - 1.
#
#
# Return the minimum number of operations needed for n to become 1.
#
#
# Example 1:
#
#
# Input: n = 8
# Output: 3
# Explanation: 8 -> 4 -> 2 -> 1
#
#
# Example 2:
#
#
# Input: n = 7
# Output: 4
# Explanation: 7 -> 8 -> 4 -> 2 -> 1
# or 7 -> 6 -> 3 -> 2 -> 1
#
#
# Example 3:
#
#
# Input: n = 4
# Output: 2
#
#
#
# Constraints:
#
#
# 1 <= n <= 2^31 - 1
#
#
#

# @lc tags=math;bit-manipulation

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定一个数，对偶数变为一半，对奇数可变为值加一或减一，求到1的最少步骤。
# 递归，备忘录。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    d = {}

    def integerReplacement(self, n: int) -> int:
        if n in self.d:
            return self.d[n]
        if n == 1:
            return 0
        r = 1
        if n % 2 == 0:
            r += self.integerReplacement(n // 2)
        else:
            r += min(self.integerReplacement(n + 1),
                     self.integerReplacement(n - 1))
        self.d[n] = r
        return r
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('n = 8')
    print('Exception :')
    print('3')
    print('Output :')
    print(str(Solution().integerReplacement(8)))
    print()

    print('Example 2:')
    print('Input : ')
    print('n = 7')
    print('Exception :')
    print('4')
    print('Output :')
    print(str(Solution().integerReplacement(7)))
    print()

    print('Example 3:')
    print('Input : ')
    print('n = 4')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().integerReplacement(4)))
    print()

    pass
# @lc main=end