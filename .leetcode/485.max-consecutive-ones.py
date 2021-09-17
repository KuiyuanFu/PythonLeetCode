# @lc app=leetcode id=485 lang=python3
#
# [485] Max Consecutive Ones
#
# https://leetcode.com/problems/max-consecutive-ones/description/
#
# algorithms
# Easy (53.45%)
# Likes:    1712
# Dislikes: 390
# Total Accepted:    486.2K
# Total Submissions: 908.5K
# Testcase Example:  '[1,1,0,1,1,1]'
#
# Given a binary array nums, return the maximum number of consecutive 1's in
# the array.
#
#
# Example 1:
#
#
# Input: nums = [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive
# 1s. The maximum number of consecutive 1s is 3.
#
#
# Example 2:
#
#
# Input: nums = [1,0,1,1,0,1]
# Output: 2
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 10^5
# nums[i] is either 0 or 1.
#
#
#

# @lc tags=array

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 求连续最长的1的个数。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        r = 0
        nums.append(0)
        for n in nums:
            if n == 1:
                r += 1
            else:
                res = max(res, r)
                r = 0
        return res
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [1,1,0,1,1,1]')
    print('Exception :')
    print('3')
    print('Output :')
    print(str(Solution().findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1])))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums = [1,0,1,1,0,1]')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().findMaxConsecutiveOnes([1, 0, 1, 1, 0, 1])))
    print()

    pass
# @lc main=end