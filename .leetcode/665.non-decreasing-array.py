# @lc app=leetcode id=665 lang=python3
#
# [665] Non-decreasing Array
#
# https://leetcode.com/problems/non-decreasing-array/description/
#
# algorithms
# Medium (21.06%)
# Likes:    3304
# Dislikes: 653
# Total Accepted:    160.6K
# Total Submissions: 760.3K
# Testcase Example:  '[4,2,3]'
#
# Given an array nums with n integers, your task is to check if it could become
# non-decreasing by modifying at most one element.
#
# We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for
# every i (0-based) such that (0 <= i <= n - 2).
#
#
# Example 1:
#
#
# Input: nums = [4,2,3]
# Output: true
# Explanation: You could modify the first 4 to 1 to get a non-decreasing
# array.
#
#
# Example 2:
#
#
# Input: nums = [4,2,1]
# Output: false
# Explanation: You can't get a non-decreasing array by modify at most one
# element.
#
#
#
# Constraints:
#
#
# n == nums.length
# 1 <= n <= 10^4
# -10^5 <= nums[i] <= 10^5
#
#
#

# @lc tags=array

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定数组，只改变一个数字的情况下，是否可以将其改变为非严格递增数列。
# 当一对违反规则时，可以将这两个值变为其中一个，来满足条件。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        f = True
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                if not f:
                    return False
                else:
                    f = False
                    if i == 1:
                        continue
                    else:
                        # lower than nums[i-2] mean that
                        # the value need least equal before
                        if nums[i] < nums[i - 2]:
                            nums[i] = nums[i - 1]
                        # change the before value to the value
                        else:
                            continue
        return True
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print(str(Solution().checkPossibility([3, 4, 2, 3])))
    print(str(Solution().checkPossibility([-1, 4, 2, 3])))
    print('Example 1:')
    print('Input : ')
    print('nums = [4,2,3]')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().checkPossibility([4, 2, 3])))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums = [4,2,1]')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().checkPossibility([4, 2, 1])))
    print()

    pass
# @lc main=end