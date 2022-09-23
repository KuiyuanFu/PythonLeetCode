# @lc app=leetcode id=982 lang=python3
#
# [982] Triples with Bitwise AND Equal To Zero
#
# https://leetcode.com/problems/triples-with-bitwise-and-equal-to-zero/description/
#
# algorithms
# Hard (57.67%)
# Likes:    302
# Dislikes: 194
# Total Accepted:    13.4K
# Total Submissions: 23.2K
# Testcase Example:  '[2,1,3]'
#
# Given an integer array nums, return the number of AND triples.
#
# An AND triple is a triple of indices (i, j, k) such that:
#
#
# 0 <= i < nums.length
# 0 <= j < nums.length
# 0 <= k < nums.length
# nums[i] & nums[j] & nums[k] == 0, where & represents the bitwise-AND
# operator.
#
#
#
# Example 1:
#
#
# Input: nums = [2,1,3]
# Output: 12
# Explanation: We could choose the following i, j, k triples:
# (i=0, j=0, k=1) : 2 & 2 & 1
# (i=0, j=1, k=0) : 2 & 1 & 2
# (i=0, j=1, k=1) : 2 & 1 & 1
# (i=0, j=1, k=2) : 2 & 1 & 3
# (i=0, j=2, k=1) : 2 & 3 & 1
# (i=1, j=0, k=0) : 1 & 2 & 2
# (i=1, j=0, k=1) : 1 & 2 & 1
# (i=1, j=0, k=2) : 1 & 2 & 3
# (i=1, j=1, k=0) : 1 & 1 & 2
# (i=1, j=2, k=0) : 1 & 3 & 2
# (i=2, j=0, k=1) : 3 & 2 & 1
# (i=2, j=1, k=0) : 3 & 1 & 2
#
#
# Example 2:
#
#
# Input: nums = [0,0,0]
# Output: 27
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 1000
# 0 <= nums[i] < 2^16
#
#
#

# @lc tags=array

# @lc imports=start
from json.encoder import INFINITY
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定数组，求三元组，使交为0，求元组个数。
# 统计每个值的个数。
# 直接暴力计数可解。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:

    def countTriplets(self, nums: List[int]) -> int:

        res = 0
        counter = Counter(nums)
        items = list(counter.items())
        twoNumsAnd = defaultdict(int)
        for i, j in product(range(len(items)), range(len(items))):
            ni, ci = items[i]
            nj, cj = items[j]
            n = ni & nj
            twoNumsAnd[n] += ci * cj
        twoNumsAndItems = list(twoNumsAnd.items())
        for i, j in product(range(len(twoNumsAndItems)), range(len(items))):
            ni, ci = twoNumsAndItems[i]
            nj, cj = items[j]
            n = ni & nj
            if n == 0:
                res += ci * cj
        return res
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [2,1,3]')
    print('Exception :')
    print('12')
    print('Output :')
    print(str(Solution().countTriplets([2, 1, 3])))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums = [0,0,0]')
    print('Exception :')
    print('27')
    print('Output :')
    print(str(Solution().countTriplets([0, 0, 0])))
    print()

    pass
# @lc main=end