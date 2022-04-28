# @lc app=leetcode id=903 lang=python3
#
# [903] Valid Permutations for DI Sequence
#
# https://leetcode.com/problems/valid-permutations-for-di-sequence/description/
#
# algorithms
# Hard (57.00%)
# Likes:    451
# Dislikes: 35
# Total Accepted:    10.7K
# Total Submissions: 18.7K
# Testcase Example:  '"DID"'
#
# You are given a string s of length n where s[i] is either:
#
#
# 'D' means decreasing, or
# 'I' means increasing.
#
#
# A permutation perm of n + 1 integers of all the integers in the range [0, n]
# is called a valid permutation if for all valid i:
#
#
# If s[i] == 'D', then perm[i] > perm[i + 1], and
# If s[i] == 'I', then perm[i] < perm[i + 1].
#
#
# Return the number of valid permutations perm. Since the answer may be large,
# return it modulo 10^9 + 7.
#
#
# Example 1:
#
#
# Input: s = "DID"
# Output: 5
# Explanation: The 5 valid permutations of (0, 1, 2, 3) are:
# (1, 0, 3, 2)
# (2, 0, 3, 1)
# (2, 1, 3, 0)
# (3, 0, 2, 1)
# (3, 1, 2, 0)
#
#
# Example 2:
#
#
# Input: s = "D"
# Output: 1
#
#
#
# Constraints:
#
#
# n == s.length
# 1 <= n <= 200
# s[i] is either 'I' or 'D'.
#
#
#

# @lc tags=random;rejection-sampling

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定1-n，与特定的大小顺序，问有多少中排列方式。
# 只与相对大小有关。dp，存储相对位置上的排列个数。就是还有多少个值大于此值时的排列个数。
#
# @lc idea=end

# @lc group=

# @lc rank=10


# @lc code=start
class Solution:

    def numPermsDISequence(self, s: str) -> int:
        length = len(s)
        dp = [1 for _ in range(length + 1)]
        for usedCounts, c in enumerate(s):
            dpn = [0] * (length - usedCounts)
            if c == 'I':
                for biggerCounts, permCounts in enumerate(dp):

                    for biggerCountsN in range(biggerCounts):
                        dpn[biggerCountsN] += permCounts

                pass
            else:
                for biggerCounts, permCounts in enumerate(dp):
                    smallerCounts = length - usedCounts - biggerCounts
                    for biggerCountsN in range(biggerCounts,
                                               biggerCounts + smallerCounts):
                        dpn[biggerCountsN] += permCounts
                pass
            dp = dpn

        return dp[0] % 1000000007

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('s = "DID"')
    print('Exception :')
    print('5')
    print('Output :')
    print(str(Solution().numPermsDISequence("DID")))
    print()

    print('Example 2:')
    print('Input : ')
    print('s = "D"')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().numPermsDISequence("D")))
    print()
    print(str(Solution().numPermsDISequence("DDDDIIIDIDIDIDIDIDIDIIIDIDIDID")))
    pass
# @lc main=end