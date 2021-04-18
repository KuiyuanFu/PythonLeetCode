# @lc app=leetcode id=31 lang=python3
#
# [31] Next Permutation
#
# https://leetcode.com/problems/next-permutation/description/
#
# algorithms
# Medium (33.88%)
# Likes:    5301
# Dislikes: 1823
# Total Accepted:    499.6K
# Total Submissions: 1.5M
# Testcase Example:  '[1,2,3]'
#
# Implement next permutation, which rearranges numbers into the
# lexicographically next greater permutation of numbers.
#
# If such an arrangement is not possible, it must rearrange it as the lowest
# possible order (i.e., sorted in ascending order).
#
# The replacement must be in place and use only constant extra memory.
#
#
# Example 1:
# Input: nums = [1,2,3]
# Output: [1,3,2]
# Example 2:
# Input: nums = [3,2,1]
# Output: [1,2,3]
# Example 3:
# Input: nums = [1,1,5]
# Output: [1,5,1]
# Example 4:
# Input: nums = [1]
# Output: [1]
#
#
# Constraints:
#
#
# 1 <= nums.length <= 100
# 0 <= nums[i] <= 100
#
#
#
#
#

# @lc tags=array

# @lc imports=start
from imports import *
# @lc imports=end

# @lc idea=start
#
# 求下一个排列，按照字典顺序，溢出则返回第一个。
# 首先，若是所有关键字都是逆序的，那么则要返回正序的。
# 其次，从后向前找逆序的长度，之后将上一个关键字换成逆序中，满足差值最小，比其大的关键字。之后把逆序变成正序。
#
# @lc idea=end

# @lc group=

# @lc rank=

# @lc code=start
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        if len(nums) < 2:
            return
        # 找逆序
        l = len(nums)-1
        for i in range(len(nums)-1, 0, -1):
            if nums[l-1] >= nums[l]:
                l -= 1
            else:
                break
        # 变成正序
        for i in range((len(nums) - l  )//2):
            nums[l+i], nums[len(nums)-1 - i] = nums[len(nums)-1 - i], nums[l+i]

        # 不全为逆序
        if l != 0:
            import bisect
            index = bisect.bisect(nums, nums[l-1], l)
            nums[l-1], nums[index] = nums[index], nums[l-1]
        return nums

        pass
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [1,2,3]')
    print('Output :')
    print(str(Solution().nextPermutation([1,2,3])))
    print('Exception :')
    print('[1,3,2]')
    print()
    
    print('Example 2:')
    print('Input : ')
    print('nums = [3,2,1]')
    print('Output :')
    print(str(Solution().nextPermutation([3,2,1])))
    print('Exception :')
    print('[1,2,3]')
    print()
    
    print('Example 3:')
    print('Input : ')
    print('nums = [1,1,5]')
    print('Output :')
    print(str(Solution().nextPermutation([1,1,5])))
    print('Exception :')
    print('[1,5,1]')
    print()
    
    print('Example 4:')
    print('Input : ')
    print('nums = [1]')
    print('Output :')
    print(str(Solution().nextPermutation([1])))
    print('Exception :')
    print('[1]')
    print()
    
    pass
# @lc main=end