# @lc app=leetcode id=77 lang=python3
#
# [77] Combinations
#
# https://leetcode.com/problems/combinations/description/
#
# algorithms
# Medium (58.10%)
# Likes:    2202
# Dislikes: 82
# Total Accepted:    360.2K
# Total Submissions: 619.6K
# Testcase Example:  '4\n2'
#
# Given two integers n and k, return all possible combinations of k numbers out
# of the range [1, n].
#
# You may return the answer in any order.
#
#
# Example 1:
#
#
# Input: n = 4, k = 2
# Output:
# [
# ⁠ [2,4],
# ⁠ [3,4],
# ⁠ [2,3],
# ⁠ [1,2],
# ⁠ [1,3],
# ⁠ [1,4],
# ]
#
#
# Example 2:
#
#
# Input: n = 1, k = 1
# Output: [[1]]
#
#
#
# Constraints:
#
#
# 1 <= n <= 20
# 1 <= k <= n
#
#
#

# @lc tags=backtracking

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定两个正整数 n，k，n表示取值范围，k表示排列个数，求 C n k 的具体排列。
# 为了保证排列唯一，每一次都指定第一位的数值，之后的所有位都要小于这个值。
# 使用递归，每次指定第一位为i，那么递归输入的就是 i-1，k-1。对返回的结果进行组合。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if k == 1:
            return [[i] for i in range(1, n + 1)]

        result = []

        for i in reversed(range(k - 1, n + 1)):
            ls = self.combine(i - 1, k - 1)
            result += [[i] + l for l in ls]
        return result


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('n = 4, k = 2')
    print('Output :')
    print(str(Solution().combine(4, 2)))
    print('Exception :')
    print('[⁠ [2,4],⁠ [3,4],⁠ [2,3],⁠ [1,2],⁠ [1,3],⁠ [1,4],]')
    print()

    print('Example 2:')
    print('Input : ')
    print('n = 1, k = 1')
    print('Output :')
    print(str(Solution().combine(1, 1)))
    print('Exception :')
    print('[[1]]')
    print()

    pass
# @lc main=end