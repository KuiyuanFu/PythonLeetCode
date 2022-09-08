# @lc app=leetcode id=967 lang=python3
#
# [967] Numbers With Same Consecutive Differences
#
# https://leetcode.com/problems/numbers-with-same-consecutive-differences/description/
#
# algorithms
# Medium (47.94%)
# Likes:    2441
# Dislikes: 183
# Total Accepted:    108K
# Total Submissions: 190.3K
# Testcase Example:  '3\n7'
#
# Return all non-negative integers of length n such that the absolute
# difference between every two consecutive digits is k.
#
# Note that every number in the answer must not have leading zeros. For
# example, 01 has one leading zero and is invalid.
#
# You may return the answer in any order.
#
#
# Example 1:
#
#
# Input: n = 3, k = 7
# Output: [181,292,707,818,929]
# Explanation: Note that 070 is not a valid number, because it has leading
# zeroes.
#
#
# Example 2:
#
#
# Input: n = 2, k = 1
# Output: [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]
#
#
#
# Constraints:
#
#
# 2 <= n <= 9
# 0 <= k <= 9
#
#
#

# @lc tags=dynamic-programming

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定位数，以及相邻位差值，求有多少个这样的数字。
# 直接dp，保存尾数。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:

    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:

        rl = list(range(10))
        # from idices
        fi = []
        for i in rl:
            t = []
            if i + k < 10:
                t.append(i + k)
            if 0 <= i - k != i + k:
                t.append(i - k)
            fi.append(t)
        # dp, end with i
        dp = [[i] for i in rl]
        dp[0] = []
        # iter
        for _ in range(n - 1):
            dp = [[n * 10 + i for j in fi[i] for n in dp[j]] for i in rl]
        return [j for i in rl for j in dp[i]]
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('n = 3, k = 7')
    print('Exception :')
    print('[181,292,707,818,929]')
    print('Output :')
    print(str(Solution().numsSameConsecDiff(3, 7)))
    print()

    print('Example 2:')
    print('Input : ')
    print('n = 2, k = 1')
    print('Exception :')
    print('[10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]')
    print('Output :')
    print(str(Solution().numsSameConsecDiff(2, 1)))
    print()

    pass
# @lc main=end