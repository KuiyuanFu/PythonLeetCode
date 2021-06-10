# @lc app=leetcode id=189 lang=python3
#
# [189] Rotate Array
#
# https://leetcode.com/problems/rotate-array/description/
#
# algorithms
# Medium (36.84%)
# Likes:    4764
# Dislikes: 941
# Total Accepted:    702.8K
# Total Submissions: 1.9M
# Testcase Example:  '[1,2,3,4,5,6,7]\n3'
#
# Given an array, rotate the array to the right by k steps, where k is
# non-negative.
#
#
# Example 1:
#
#
# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]
#
#
# Example 2:
#
#
# Input: nums = [-1,-100,3,99], k = 2
# Output: [3,99,-1,-100]
# Explanation:
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 10^5
# -2^31 <= nums[i] <= 2^31 - 1
# 0 <= k <= 10^5
#
#
#
# Follow up:
#
#
# Try to come up with as many solutions as you can. There are at least three
# different ways to solve this problem.
# Could you do it in-place with O(1) extra space?
#
#
#

# @lc tags=array

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 从给定的位置，旋转数组。
# 一种很巧妙的思想，是使用三次反转来达到旋转的目的。
# 旋转，就是将后k个，移动到前面。
# 首先反转后k个，这样倒数第k个就移动到了最后一个。
# 之后反转前n-k个，这样整数第n-k个就移动到了第一个。
# 之后整体反转，就达到了旋转的目的。
#
# @lc idea=end

# @lc group=array

# @lc rank=10


# @lc code=start
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n
        nums[:n - k] = reversed(nums[:n - k])
        nums[n - k:] = reversed(nums[n - k:])
        nums[:] = reversed(nums)
        return nums

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [1,2,3,4,5,6,7], k = 3')
    print('Exception :')
    print('[5,6,7,1,2,3,4]')
    print('Output :')
    print(str(Solution().rotate([1, 2, 3, 4, 5, 6, 7], 3)))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums = [-1,-100,3,99], k = 2')
    print('Exception :')
    print('[3,99,-1,-100]')
    print('Output :')
    print(str(Solution().rotate([-1, -100, 3, 99], 2)))
    print()

    pass
# @lc main=end