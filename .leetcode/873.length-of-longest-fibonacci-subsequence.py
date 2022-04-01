# @lc app=leetcode id=873 lang=python3
#
# [873] Length of Longest Fibonacci Subsequence
#
# https://leetcode.com/problems/length-of-longest-fibonacci-subsequence/description/
#
# algorithms
# Medium (48.59%)
# Likes:    1393
# Dislikes: 50
# Total Accepted:    47.1K
# Total Submissions: 97K
# Testcase Example:  '[1,2,3,4,5,6,7,8]'
#
# A sequence x1, x2, ..., xn is Fibonacci-like if:
#
#
# n >= 3
# xi + xi+1 == xi+2 for all i + 2 <= n
#
#
# Given a strictly increasing array arr of positive integers forming a
# sequence, return the length of the longest Fibonacci-like subsequence of arr.
# If one does not exist, return 0.
#
# A subsequence is derived from another sequence arr by deleting any number of
# elements (including none) from arr, without changing the order of the
# remaining elements. For example, [3, 5, 8] is a subsequence of [3, 4, 5, 6,
# 7, 8].
#
#
# Example 1:
#
#
# Input: arr = [1,2,3,4,5,6,7,8]
# Output: 5
# Explanation: The longest subsequence that is fibonacci-like: [1,2,3,5,8].
#
# Example 2:
#
#
# Input: arr = [1,3,7,11,12,14,18]
# Output: 3
# Explanation: The longest subsequence that is fibonacci-like: [1,11,12],
# [3,11,14] or [7,11,18].
#
#
# Constraints:
#
#
# 3 <= arr.length <= 1000
# 1 <= arr[i] < arr[i + 1] <= 10^9
#
#
#

# @lc tags=minimax

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定严格递增数组，求满足类似fabonacci的数组的最长长度
# dp 存储的是从i到j的数组长度。
#
# @lc idea=end

# @lc group=minimax

# @lc rank=10


# @lc code=start
class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        length = len(arr)
        res = 0
        dp = [[0 for _ in range(length)] for _ in range(length)]
        for i in range(2, length):
            l, r = 0, i - 1
            while l < r:
                s = arr[l] + arr[r]
                if s > arr[i]:
                    r -= 1
                elif s < arr[i]:
                    l += 1
                else:
                    dp[r][i] = dp[l][r] + 1
                    res = max(res, dp[r][i])
                    r -= 1
                    l += 1
        return res + 2 if res else 0
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('arr = [1,2,3,4,5,6,7,8]')
    print('Exception :')
    print('5')
    print('Output :')
    print(str(Solution().lenLongestFibSubseq([1, 2, 3, 4, 5, 6, 7, 8])))
    print()

    print('Example 2:')
    print('Input : ')
    print('arr = [1,3,7,11,12,14,18]')
    print('Exception :')
    print('3')
    print('Output :')
    print(str(Solution().lenLongestFibSubseq([1, 3, 7, 11, 12, 14, 18])))
    print()

    pass
# @lc main=end