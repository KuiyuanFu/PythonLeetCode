# @lc app=leetcode id=414 lang=python3
#
# [414] Third Maximum Number
#
# https://leetcode.com/problems/third-maximum-number/description/
#
# algorithms
# Easy (30.83%)
# Likes:    1224
# Dislikes: 1968
# Total Accepted:    256.6K
# Total Submissions: 831.3K
# Testcase Example:  '[3,2,1]'
#
# Given integer array nums, return the third maximum number in this array. If
# the third maximum does not exist, return the maximum number.
#
#
# Example 1:
#
#
# Input: nums = [3,2,1]
# Output: 1
# Explanation: The third maximum is 1.
#
#
# Example 2:
#
#
# Input: nums = [1,2]
# Output: 2
# Explanation: The third maximum does not exist, so the maximum (2) is returned
# instead.
#
#
# Example 3:
#
#
# Input: nums = [2,2,3,1]
# Output: 1
# Explanation: Note that the third maximum here means the third maximum
# distinct number.
# Both numbers with value 2 are both considered as second maximum.
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 10^4
# -2^31 <= nums[i] <= 2^31 - 1
#
#
#
# Follow up: Can you find an O(n) solution?
#

# @lc tags=array

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 求第三大的元素。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = set(nums)
        if len(nums) < 3:
            return max(nums)
        h = [-2**31, -2**31, -2**31]
        for n in nums:
            heappushpop(h, n)
        return h[0]
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [3,2,1]')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().thirdMax([3, 2, 1])))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums = [1,2]')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().thirdMax([1, 2])))
    print()

    print('Example 3:')
    print('Input : ')
    print('nums = [2,2,3,1]')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().thirdMax([2, 2, 3, 1])))
    print()

    pass
# @lc main=end