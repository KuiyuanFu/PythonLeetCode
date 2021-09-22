# @lc app=leetcode id=526 lang=python3
#
# [526] Beautiful Arrangement
#
# https://leetcode.com/problems/beautiful-arrangement/description/
#
# algorithms
# Medium (62.77%)
# Likes:    1626
# Dislikes: 237
# Total Accepted:    103.4K
# Total Submissions: 164.3K
# Testcase Example:  '2'
#
# Suppose you have n integers labeled 1 through n. A permutation of those n
# integers perm (1-indexed) is considered a beautiful arrangement if for every
# i (1 <= i <= n), either of the following is true:
#
#
# perm[i] is divisible by i.
# i is divisible by perm[i].
#
#
# Given an integer n, return the number of the beautiful arrangements that you
# can construct.
#
#
# Example 1:
#
#
# Input: n = 2
# Output: 2
# Explanation:
# The first beautiful arrangement is [1,2]:
# ⁠   - perm[1] = 1 is divisible by i = 1
# ⁠   - perm[2] = 2 is divisible by i = 2
# The second beautiful arrangement is [2,1]:
# ⁠   - perm[1] = 2 is divisible by i = 1
# ⁠   - i = 2 is divisible by perm[2] = 1
#
#
# Example 2:
#
#
# Input: n = 1
# Output: 1
#
#
#
# Constraints:
#
#
# 1 <= n <= 15
#
#
#

# @lc tags=backtracking

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 求置换后，每一个位置上的数都可以整除或被整除索引值，的置换个数。
# 暴力。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def countArrangement(self, n: int) -> int:

        perfects = [[i] for i in range(n)]
        flags = [True] * n
        for i in range(n):
            ni = i + 1
            for j in range(i + 1, n):
                nj = j + 1
                if ni % nj == 0 or nj % ni == 0:
                    perfects[i].append(j)
                    perfects[j].append(i)

        def recur(idx):
            if idx == n:
                return 1

            res = 0
            for i in perfects[idx]:
                if flags[i]:
                    flags[i] = False
                    res += recur(idx + 1)
                    flags[i] = True
            return res

        return recur(0)
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('n = 2')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().countArrangement(2)))
    print()

    print('Example 2:')
    print('Input : ')
    print('n = 1')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().countArrangement(1)))
    print()

    pass
# @lc main=end