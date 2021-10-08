# @lc app=leetcode id=646 lang=python3
#
# [646] Maximum Length of Pair Chain
#
# https://leetcode.com/problems/maximum-length-of-pair-chain/description/
#
# algorithms
# Medium (54.45%)
# Likes:    1801
# Dislikes: 95
# Total Accepted:    92.6K
# Total Submissions: 169.4K
# Testcase Example:  '[[1,2],[2,3],[3,4]]'
#
# You are given an array of n pairs pairs where pairs[i] = [lefti, righti] and
# lefti < righti.
#
# A pair p2 = [c, d] follows a pair p1 = [a, b] if b < c. A chain of pairs can
# be formed in this fashion.
#
# Return the length longest chain which can be formed.
#
# You do not need to use up all the given intervals. You can select pairs in
# any order.
#
#
# Example 1:
#
#
# Input: pairs = [[1,2],[2,3],[3,4]]
# Output: 2
# Explanation: The longest chain is [1,2] -> [3,4].
#
#
# Example 2:
#
#
# Input: pairs = [[1,2],[7,8],[4,5]]
# Output: 3
# Explanation: The longest chain is [1,2] -> [4,5] -> [7,8].
#
#
#
# Constraints:
#
#
# n == pairs.length
# 1 <= n <= 1000
# -1000 <= lefti < righti <= 1000
#
#
#

# @lc tags=dynamic-programming

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 区间，最多数量不重合。
# 贪心。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        if len(pairs) <= 1:
            return len(pairs)
        pairs.sort()
        res = [[-1000, 1000]]
        for l, r in pairs:
            if l > res[-1][-1]:
                res.append([l, r])
            else:
                res[-1][-1] = min(res[-1][-1], r)
        return len(res)

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('pairs = [[1,2],[2,3],[3,4]]')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().findLongestChain([[1, 2], [2, 3], [3, 4]])))
    print()

    print('Example 2:')
    print('Input : ')
    print('pairs = [[1,2],[7,8],[4,5]]')
    print('Exception :')
    print('3')
    print('Output :')
    print(str(Solution().findLongestChain([[1, 2], [7, 8], [4, 5]])))
    print()

    pass
# @lc main=end