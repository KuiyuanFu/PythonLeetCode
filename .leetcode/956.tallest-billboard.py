# @lc app=leetcode id=956 lang=python3
#
# [956] Tallest Billboard
#
# https://leetcode.com/problems/tallest-billboard/description/
#
# algorithms
# Hard (39.83%)
# Likes:    768
# Dislikes: 27
# Total Accepted:    14.4K
# Total Submissions: 36.2K
# Testcase Example:  '[1,2,3,6]'
#
# You are installing a billboard and want it to have the largest height. The
# billboard will have two steel supports, one on each side. Each steel support
# must be an equal height.
#
# You are given a collection of rods that can be welded together. For example,
# if you have rods of lengths 1, 2, and 3, you can weld them together to make a
# support of length 6.
#
# Return the largest possible height of your billboard installation. If you
# cannot support the billboard, return 0.
#
#
# Example 1:
#
#
# Input: rods = [1,2,3,6]
# Output: 6
# Explanation: We have two disjoint subsets {1,2,3} and {6}, which have the
# same sum = 6.
#
#
# Example 2:
#
#
# Input: rods = [1,2,3,4,5,6]
# Output: 10
# Explanation: We have two disjoint subsets {2,3,5} and {4,6}, which have the
# same sum = 10.
#
#
# Example 3:
#
#
# Input: rods = [1,2]
# Output: 0
# Explanation: The billboard cannot be supported, so we return 0.
#
#
#
# Constraints:
#
#
# 1 <= rods.length <= 20
# 1 <= rods[i] <= 1000
# sum(rods[i]) <= 5000
#
#
#

# @lc tags=dynamic-programming

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定数组，可以合并元素，得到两个相同的元素，求相同元素的最大值。
# 记录差值对应的最高基准。
#
# @lc idea=end

# @lc group=

# @lc rank=8


# @lc code=start
class Solution:

    def tallestBillboard(self, rods: List[int]) -> int:

        diffDict = {0: 0}
        newDiffDict = {}

        def add(d, b):
            if d in diffDict:
                b = max(b, diffDict[d])
            if d in newDiffDict:
                t = newDiffDict[d]
                if b > t:
                    newDiffDict[d] = b
            else:
                newDiffDict[d] = b

        maxDiff = sum(rods)
        rods.sort()
        for rod in rods:
            maxDiff -= rod
            newDiffDict = {}

            for diff, base in diffDict.items():

                # not use
                diffNew = diff
                if diffNew <= maxDiff:
                    add(diffNew, base)

                # longer side
                diffNew = diff + rod
                if diffNew <= maxDiff:
                    add(diffNew, base)

                # shorter side
                diffNew = abs(diff - rod)
                base = base + min(diff, rod)
                if diffNew <= maxDiff:
                    add(diffNew, base)
            diffDict = newDiffDict
        return diffDict[0]

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('rods = [1,2,3,6]')
    print('Exception :')
    print('6')
    print('Output :')
    print(str(Solution().tallestBillboard([1, 2, 3, 6])))
    print()

    print('Example 2:')
    print('Input : ')
    print('rods = [1,2,3,4,5,6]')
    print('Exception :')
    print('10')
    print('Output :')
    print(str(Solution().tallestBillboard([1, 2, 3, 4, 5, 6])))
    print()

    print('Example 3:')
    print('Input : ')
    print('rods = [1,2]')
    print('Exception :')
    print('0')
    print('Output :')
    print(str(Solution().tallestBillboard([1, 2])))
    print()

    print('Example 3:')
    print(
        str(Solution().tallestBillboard([
            123, 124, 999, 634, 645, 234, 274, 23, 42, 34, 234, 2, 35, 35, 235,
            31, 46, 456, 3, 456
        ])))
    print()

    pass
# @lc main=end