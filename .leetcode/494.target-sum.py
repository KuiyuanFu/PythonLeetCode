# @lc app=leetcode id=494 lang=python3
#
# [494] Target Sum
#
# https://leetcode.com/problems/target-sum/description/
#
# algorithms
# Medium (45.34%)
# Likes:    5132
# Dislikes: 207
# Total Accepted:    274.7K
# Total Submissions: 607K
# Testcase Example:  '[1,1,1,1,1]\n3'
#
# You are given an integer array nums and an integer target.
#
# You want to build an expression out of nums by adding one of the symbols '+'
# and '-' before each integer in nums and then concatenate all the
# integers.
#
#
# For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1
# and concatenate them to build the expression "+2-1".
#
#
# Return the number of different expressions that you can build, which
# evaluates to target.
#
#
# Example 1:
#
#
# Input: nums = [1,1,1,1,1], target = 3
# Output: 5
# Explanation: There are 5 ways to assign symbols to make the sum of nums be
# target 3.
# -1 + 1 + 1 + 1 + 1 = 3
# +1 - 1 + 1 + 1 + 1 = 3
# +1 + 1 - 1 + 1 + 1 = 3
# +1 + 1 + 1 - 1 + 1 = 3
# +1 + 1 + 1 + 1 - 1 = 3
#
#
# Example 2:
#
#
# Input: nums = [1], target = 1
# Output: 1
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 20
# 0 <= nums[i] <= 1000
# 0 <= sum(nums[i]) <= 1000
# -1000 <= target <= 1000
#
#
#

# @lc tags=dynamic-programming;depth-first-search

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 求给定数组加上符号后能得到目标值的数量。
# 同样数字的顺序其实不重要。递归，组合。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        d = defaultdict(int)
        zn = 0
        for n in nums:
            if n == 0:
                zn += 1
            else:
                d[n] += 1
        keys = list(d.keys())
        length = len(keys)

        buffer = {}

        def recur(idx, target):
            t = (idx, target)
            if t in buffer:
                return buffer[t]
            if idx == length:
                if target == 0:
                    return 1
                else:
                    return 0
            res = 0
            n = keys[idx]
            c = d[n]
            b = -n * c

            for i in range(c + 1):
                rn = recur(idx + 1, target - b)
                if rn != 0:
                    res += rn * factorial(c) // factorial(i) // factorial(c -
                                                                          i)
                b += n * 2

            buffer[t] = res
            return res

        return recur(0, target) * (2**zn)


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [1,1,1,1,1], target = 3')
    print('Exception :')
    print('5')
    print('Output :')
    print(str(Solution().findTargetSumWays([1, 1, 1, 1, 1], 3)))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums = [1], target = 1')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().findTargetSumWays([1], 1)))
    print()

    pass
# @lc main=end