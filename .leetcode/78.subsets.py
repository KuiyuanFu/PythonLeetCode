# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#
# https://leetcode.com/problems/subsets/description/
#
# algorithms
# Medium (65.75%)
# Likes:    5618
# Dislikes: 113
# Total Accepted:    754.8K
# Total Submissions: 1.1M
# Testcase Example:  '[1,2,3]'
#
# Given an integer array nums of unique elements, return all possible subsets
# (the power set).
#
# The solution set must not contain duplicate subsets. Return the solution in
# any order.
#
#
# Example 1:
#
#
# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
#
#
# Example 2:
#
#
# Input: nums = [0]
# Output: [[],[0]]
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10
# All the numbers of nums are unique.
#
#
#

# @lc tags=array;backtracking;bit-manipulation

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定一个数字数组，元素唯一，求这个集合的幂集。
# 使用分治、递归，每次选定中间位置进行分裂，成两个子问题，再将子数组的幂集做笛卡尔积。
#
# @lc idea=end

# @lc group=

# @lc rank=6


# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        numss = [[n] for n in nums]
        return self.recur(numss)
        pass

    def recur(self, numss: List[List[int]]) -> List[List[int]]:
        if len(numss) == 1 and len(numss[0]) != 0:
            return numss + [[]]

        ls = self.recur(numss[:len(numss) // 2])
        rs = self.recur(numss[len(numss) // 2:])
        result = [l + r for l in ls for r in rs]
        return result


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [1,2,3]')
    print('Output :')
    print(str(Solution().subsets([1, 2, 3])))
    print('Exception :')
    print('[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]')
    print()

    print('Example 2:')
    print('Input : ')
    print('nums = [0]')
    print('Output :')
    print(str(Solution().subsets([0])))
    print('Exception :')
    print('[[],[0]]')
    print()

    pass
# @lc main=end