# @lc app=leetcode id=645 lang=python3
#
# [645] Set Mismatch
#
# https://leetcode.com/problems/set-mismatch/description/
#
# algorithms
# Easy (40.98%)
# Likes:    1425
# Dislikes: 493
# Total Accepted:    144.8K
# Total Submissions: 352.7K
# Testcase Example:  '[1,2,2,4]'
#
# You have a set of integers s, which originally contains all the numbers from
# 1 to n. Unfortunately, due to some error, one of the numbers in s got
# duplicated to another number in the set, which results in repetition of one
# number and loss of another number.
#
# You are given an integer array nums representing the data status of this set
# after the error.
#
# Find the number that occurs twice and the number that is missing and return
# them in the form of an array.
#
#
# Example 1:
# Input: nums = [1,2,2,4]
# Output: [2,3]
# Example 2:
# Input: nums = [1,1]
# Output: [1,2]
#
#
# Constraints:
#
#
# 2 <= nums.length <= 10^4
# 1 <= nums[i] <= 10^4
#
#
#

# @lc tags=hash-table;math

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 数组原始包含1-n，但由于错误，导致一个元素转换为了另一个元素，找重复的数字和缺少的数字。
# 翻转标记。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        # duplicate the bigger
        f = sum(nums) - (1 + len(nums)) * len(nums) // 2 > 0
        res = [0, 0]
        for n in nums:
            nums[abs(n) - 1] = -nums[abs(n) - 1]
        for i, n in enumerate(nums):
            if n > 0:
                if f:
                    res[1] = i + 1
                else:
                    res[0] = i + 1
                f = not f
        return res
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [1,2,2,4]')
    print('Exception :')
    print('[2,3]')
    print('Output :')
    print(str(Solution().findErrorNums([1, 2, 2, 4])))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums = [1,1]')
    print('Exception :')
    print('[1,2]')
    print('Output :')
    print(str(Solution().findErrorNums([1, 1])))
    print()
    print(str(Solution().findErrorNums([2, 2])))
    pass
# @lc main=end