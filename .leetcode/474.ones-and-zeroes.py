# @lc app=leetcode id=474 lang=python3
#
# [474] Ones and Zeroes
#
# https://leetcode.com/problems/ones-and-zeroes/description/
#
# algorithms
# Medium (43.74%)
# Likes:    2264
# Dislikes: 307
# Total Accepted:    92.4K
# Total Submissions: 211.1K
# Testcase Example:  '["10","0001","111001","1","0"]\n5\n3'
#
# You are given an array of binary strings strs and two integers m and n.
#
# Return the size of the largest subset of strs such that there are at most m
# 0's and n 1's in the subset.
#
# A set x is a subset of a set y if all elements of x are also elements of
# y.
#
#
# Example 1:
#
#
# Input: strs = ["10","0001","111001","1","0"], m = 5, n = 3
# Output: 4
# Explanation: The largest subset with at most 5 0's and 3 1's is {"10",
# "0001", "1", "0"}, so the answer is 4.
# Other valid but smaller subsets include {"0001", "1"} and {"10", "1", "0"}.
# {"111001"} is an invalid subset because it contains 4 1's, greater than the
# maximum of 3.
#
#
# Example 2:
#
#
# Input: strs = ["10","0","1"], m = 1, n = 1
# Output: 2
# Explanation: The largest subset is {"0", "1"}, so the answer is 2.
#
#
#
# Constraints:
#
#
# 1 <= strs.length <= 600
# 1 <= strs[i].length <= 100
# strs[i] consists only of digits '0' and '1'.
# 1 <= m, n <= 100
#
#
#

# @lc tags=dynamic-programming

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定二进制字符串，之后给定1与0的最多个数，求子集满足1与0数量不大于给定数量的最多个数。
# 这个的思路不是依次迭代dpbuffer，而是根据输入来更新。
#
# @lc idea=end

# @lc group=dynamic-programming

# @lc rank=10


# @lc code=start
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        for s in strs:
            mc, nc = s.count('0'), s.count('1')
            for i, j in product(range(m, mc - 1, -1), range(n, nc - 1, -1)):
                dp[i][j] = max(dp[i][j], dp[i - mc][j - nc] + 1)

        return dp[-1][-1]
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('strs = ["10","0001","111001","1","0"], m = 5, n = 3')
    print('Exception :')
    print('4')
    print('Output :')
    print(str(Solution().findMaxForm(["10", "0001", "111001", "1", "0"], 5,
                                     3)))
    print()

    print('Example 2:')
    print('Input : ')
    print('strs = ["10","0","1"], m = 1, n = 1')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().findMaxForm(["10", "0", "1"], 1, 1)))
    print()
    print(
        str(Solution().findMaxForm(["11111", "100", "1101", "1101", "11000"],
                                   5, 7)))

    pass
# @lc main=end