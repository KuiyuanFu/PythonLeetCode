# @lc app=leetcode id=216 lang=python3
#
# [216] Combination Sum III
#
# https://leetcode.com/problems/combination-sum-iii/description/
#
# algorithms
# Medium (61.09%)
# Likes:    1937
# Dislikes: 67
# Total Accepted:    233.8K
# Total Submissions: 381.4K
# Testcase Example:  '3\n7'
#
# Find all valid combinations of k numbers that sum up to n such that the
# following conditions are true:
#
#
# Only numbers 1 through 9 are used.
# Each number is used at most once.
#
#
# Return a list of all possible valid combinations. The list must not contain
# the same combination twice, and the combinations may be returned in any
# order.
#
#
# Example 1:
#
#
# Input: k = 3, n = 7
# Output: [[1,2,4]]
# Explanation:
# 1 + 2 + 4 = 7
# There are no other valid combinations.
#
# Example 2:
#
#
# Input: k = 3, n = 9
# Output: [[1,2,6],[1,3,5],[2,3,4]]
# Explanation:
# 1 + 2 + 6 = 9
# 1 + 3 + 5 = 9
# 2 + 3 + 4 = 9
# There are no other valid combinations.
#
#
# Example 3:
#
#
# Input: k = 4, n = 1
# Output: []
# Explanation: There are no valid combinations.
# Using 4 different numbers in the range [1,9], the smallest sum we can get is
# 1+2+3+4 = 10 and since 10 > 1, there are no valid combination.
#
#
# Example 4:
#
#
# Input: k = 3, n = 2
# Output: []
# Explanation: There are no valid combinations.
#
#
# Example 5:
#
#
# Input: k = 9, n = 45
# Output: [[1,2,3,4,5,6,7,8,9]]
# Explanation:
# 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 = 45
# There are no other valid combinations.
#
#
#
# Constraints:
#
#
# 2 <= k <= 9
# 1 <= n <= 60
#
#
#

# @lc tags=array;backtracking

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定数字个数k，只能使用1-9，且不能重复，得到所有和为n的组合。
# 直接贪心算法。
# 每次选择一个数，之后选择的所有数都必须小于其，以便去重。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
        buffer = []

        def recur(m, k, n):
            if k == 0 and n == 0:
                result.append(buffer.copy())

            if (1 + k) * k // 2 > n:
                return
            buffer.append(0)
            for i in reversed(range(1, m)):
                buffer[-1] = i
                recur(i, k - 1, n - i)
            buffer.pop()
            pass

        recur(10, k, n)
        return result
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('k = 3, n = 7')
    print('Exception :')
    print('[[1,2,4]]')
    print('Output :')
    print(str(Solution().combinationSum3(3, 7)))
    print()

    print('Example 2:')
    print('Input : ')
    print('k = 3, n = 9')
    print('Exception :')
    print('[[1,2,6],[1,3,5],[2,3,4]]')
    print('Output :')
    print(str(Solution().combinationSum3(3, 9)))
    print()

    print('Example 3:')
    print('Input : ')
    print('k = 4, n = 1')
    print('Exception :')
    print('[]')
    print('Output :')
    print(str(Solution().combinationSum3(4, 1)))
    print()

    print('Example 4:')
    print('Input : ')
    print('k = 3, n = 2')
    print('Exception :')
    print('[]')
    print('Output :')
    print(str(Solution().combinationSum3(3, 2)))
    print()

    print('Example 5:')
    print('Input : ')
    print('k = 9, n = 45')
    print('Exception :')
    print('[[1,2,3,4,5,6,7,8,9]]')
    print('Output :')
    print(str(Solution().combinationSum3(9, 45)))
    print()

    pass
# @lc main=end