# @lc app=leetcode id=75 lang=python3
#
# [75] Sort Colors
#
# https://leetcode.com/problems/sort-colors/description/
#
# algorithms
# Medium (49.90%)
# Likes:    5201
# Dislikes: 298
# Total Accepted:    663.5K
# Total Submissions: 1.3M
# Testcase Example:  '[2,0,2,1,1,0]'
#
# Given an array nums with n objects colored red, white, or blue, sort them
# in-place so that objects of the same color are adjacent, with the colors in
# the order red, white, and blue.
# 
# We will use the integers 0, 1, and 2 to represent the color red, white, and
# blue, respectively.
# 
# 
# Example 1:
# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
# Example 2:
# Input: nums = [2,0,1]
# Output: [0,1,2]
# Example 3:
# Input: nums = [0]
# Output: [0]
# Example 4:
# Input: nums = [1]
# Output: [1]
# 
# 
# Constraints:
# 
# 
# n == nums.length
# 1 <= n <= 300
# nums[i] is 0, 1, or 2.
# 
# 
# 
# Follow up:
# 
# 
# Could you solve this problem without using the library's sort function?
# Could you come up with a one-pass algorithm using only O(1) constant space?
# 
# 
#


# @lc tags=array;two-pointers;sort

# @lc imports=start
from imports import *
# @lc imports=end

# @lc idea=start
# 
# 原址排序，元素只有三种取值。
# 要求一次遍历，使用恒定空间。
# 使用双指针，保证指针的一侧都是指定颜色的。
# 
# @lc idea=end

# @lc group=two-pointers

# @lc rank=6

# @lc code=start
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        l ,r = 0 ,len(nums) -1 
        p = 0
        while p <= r:
            if nums[p]  == 0:
                # 交换过来的一定是 1
                nums[p],nums[l] = nums[l],nums[p]
                l+=1
                p+=1
            elif nums[p]  == 2:
                nums[p],nums[r] = nums[r],nums[p]
                r-=1        
            else:
                p+=1
        return nums
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [2,0,2,1,1,0]')
    print('Output :')
    print(str(Solution().sortColors([2,0,2,1,1,0])))
    print('Exception :')
    print('[0,0,1,1,2,2]')
    print()
    
    print('Example 2:')
    print('Input : ')
    print('nums = [2,0,1]')
    print('Output :')
    print(str(Solution().sortColors([2,0,1])))
    print('Exception :')
    print('[0,1,2]')
    print()
    
    print('Example 3:')
    print('Input : ')
    print('nums = [0]')
    print('Output :')
    print(str(Solution().sortColors([0])))
    print('Exception :')
    print('[0]')
    print()
    
    print('Example 4:')
    print('Input : ')
    print('nums = [1]')
    print('Output :')
    print(str(Solution().sortColors([1])))
    print('Exception :')
    print('[1]')
    print()
    
    pass
# @lc main=end