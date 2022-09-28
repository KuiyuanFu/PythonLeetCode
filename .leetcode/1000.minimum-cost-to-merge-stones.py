# @lc app=leetcode id=1000 lang=python3
#
# [1000] Minimum Cost to Merge Stones
#
# https://leetcode.com/problems/minimum-cost-to-merge-stones/description/
#
# algorithms
# Hard (42.21%)
# Likes:    1886
# Dislikes: 92
# Total Accepted:    31.2K
# Total Submissions: 73.8K
# Testcase Example:  '[3,2,4,1]\n2'
#
# There are n piles of stones arranged in a row. The i^th pile has stones[i]
# stones.
#
# A move consists of merging exactly k consecutive piles into one pile, and the
# cost of this move is equal to the total number of stones in these k piles.
#
# Return the minimum cost to merge all piles of stones into one pile. If it is
# impossible, return -1.
#
#
# Example 1:
#
#
# Input: stones = [3,2,4,1], k = 2
# Output: 20
# Explanation: We start with [3, 2, 4, 1].
# We merge [3, 2] for a cost of 5, and we are left with [5, 4, 1].
# We merge [4, 1] for a cost of 5, and we are left with [5, 5].
# We merge [5, 5] for a cost of 10, and we are left with [10].
# The total cost was 20, and this is the minimum possible.
#
#
# Example 2:
#
#
# Input: stones = [3,2,4,1], k = 3
# Output: -1
# Explanation: After any merge operation, there are 2 piles left, and we can't
# merge anymore.  So the task is impossible.
#
#
# Example 3:
#
#
# Input: stones = [3,5,1,2,6], k = 3
# Output: 25
# Explanation: We start with [3, 5, 1, 2, 6].
# We merge [5, 1, 2] for a cost of 8, and we are left with [3, 8, 6].
# We merge [3, 8, 6] for a cost of 17, and we are left with [17].
# The total cost was 25, and this is the minimum possible.
#
#
#
# Constraints:
#
#
# n == stones.length
# 1 <= n <= 30
# 1 <= stones[i] <= 100
# 2 <= k <= 30
#
#
#

# @lc tags=dynamic-programming

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定数组，每次合并k长连续子序列为1个，问是否能合成一个，若能，最少代价。每次合并，代价为此序列的值的和。
# dp，保存范围内最优解
#
#
# @lc idea=end

# @lc group=dynamic-programming

# @lc rank=10


# @lc code=start
class Solution:

    def mergeStones(self, stones, k):
        length = len(stones)
        kr1 = k - 1
        if k != 2 and length % (kr1) != 1:
            return -1

        dp = [[0 for _ in range(length)] for _ in range(length)]

        ss = [0]
        for s in stones:
            ss.append(ss[-1] + s)

        for sl in range(kr1, length):
            for l in range(0, length - sl):
                r = l + sl
                t = min(dp[l][m] + dp[m + 1][r] for m in range(l, r, kr1))
                if sl % kr1 == 0:
                    t += ss[r + 1] - ss[l]
                dp[l][r] = t
        return dp[0][length - 1]


# @lc code=end

# @lc main=start
if __name__ == '__main__':

    print()
    print('Example 1:')
    print('Input : ')
    print('stones = 7, 7, 8, 6, 5, 6, 6], 3')
    print('Exception :')
    print('83')
    print('Output :')
    print(str(Solution().mergeStones([7, 7, 8, 6, 5, 6, 6], 3)))
    print()

    print('Example 1:')
    print('Input : ')
    print('stones = [3,2,4,1], k = 2')
    print('Exception :')
    print('20')
    print('Output :')
    print(str(Solution().mergeStones([3, 2, 4, 1], 2)))

    print('Example 2:')
    print('Input : ')
    print('stones = [3,2,4,1], k = 3')
    print('Exception :')
    print('-1')
    print('Output :')
    print(str(Solution().mergeStones([3, 2, 4, 1], 3)))
    print()

    print('Example 3:')
    print('Input : ')
    print('stones = [3,5,1,2,6], k = 3')
    print('Exception :')
    print('25')
    print('Output :')
    print(str(Solution().mergeStones([3, 5, 1, 2, 6], 3)))
    print()

    pass
# @lc main=end