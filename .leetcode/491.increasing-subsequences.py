# @lc app=leetcode id=491 lang=python3
#
# [491] Increasing Subsequences
#
# https://leetcode.com/problems/increasing-subsequences/description/
#
# algorithms
# Medium (49.17%)
# Likes:    1172
# Dislikes: 145
# Total Accepted:    64.1K
# Total Submissions: 130K
# Testcase Example:  '[4,6,7,7]'
#
# Given an integer array nums, return all the different possible increasing
# subsequences of the given array with at least two elements. You may return
# the answer in any order.
#
# The given array may contain duplicates, and two equal integers should also be
# considered a special case of increasing sequence.
#
#
# Example 1:
#
#
# Input: nums = [4,6,7,7]
# Output: [[4,6],[4,6,7],[4,6,7,7],[4,7],[4,7,7],[6,7],[6,7,7],[7,7]]
#
#
# Example 2:
#
#
# Input: nums = [4,4,3,2,1]
# Output: [[4,4]]
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 15
# -100 <= nums[i] <= 100
#
#
#

# @lc tags=depth-first-search

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 返回所有可能的递增序列。
# 字典，顺序遍历。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:

        ds = {}

        for n in nums:
            ls = []
            for k in ds.keys():
                if k <= n:
                    for l in ds[k]:
                        ls.append(tuple([*l, n]))
            if n not in ds:
                ds[n] = set()
            s = ds[n]
            ls.append(tuple([n]))
            for l in ls:
                s.add(l)
        res = []
        for v in ds.values():
            for l in v:
                if len(l) > 1:
                    res.append(list(l))
        return res
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [4,6,7,7]')
    print('Exception :')
    print('[[4,6],[4,6,7],[4,6,7,7],[4,7],[4,7,7],[6,7],[6,7,7],[7,7]]')
    print('Output :')
    print(str(Solution().findSubsequences([4, 6, 7, 7])))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums = [4,4,3,2,1]')
    print('Exception :')
    print('[[4,4]]')
    print('Output :')
    print(str(Solution().findSubsequences([4, 4, 3, 2, 1])))
    print()

    pass
# @lc main=end