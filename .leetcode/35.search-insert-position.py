# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#
# https://leetcode.com/problems/search-insert-position/description/
#
# algorithms
# Easy (42.86%)
# Likes:    3403
# Dislikes: 287
# Total Accepted:    802.5K
# Total Submissions: 1.9M
# Testcase Example:  '[1,3,5,6]\n5'
#
# Given a sorted array of distinct integers and a target value, return the
# index if the target is found. If not, return the index where it would be if
# it were inserted in order.
# 
# 
# Example 1:
# Input: nums = [1,3,5,6], target = 5
# Output: 2
# Example 2:
# Input: nums = [1,3,5,6], target = 2
# Output: 1
# Example 3:
# Input: nums = [1,3,5,6], target = 7
# Output: 4
# Example 4:
# Input: nums = [1,3,5,6], target = 0
# Output: 0
# Example 5:
# Input: nums = [1], target = 0
# Output: 0
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^4
# -10^4 <= nums[i] <= 10^4
# nums contains distinct values sorted in ascending order.
# -10^4 <= target <= 10^4
# 
# 
#
# 
#

# @lc tags=array;binary-search

# @lc imports=start
from imports import *
# @lc imports=end

# @lc idea=start
#
# 就是二分搜索，bisect()
#
# @lc idea=end

# @lc group=

# @lc rank=

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
         # 是否存在
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l+r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid+1
            else:
                r = mid -1
        return l 
        pass
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [1,3,5,6], target = 5')
    print('Output :')
    print(str(Solution().searchInsert([1,3,5,6],5)))
    print('Exception :')
    print('2')
    print()
    
    print('Example 2:')
    print('Input : ')
    print('nums = [1,3,5,6], target = 2')
    print('Output :')
    print(str(Solution().searchInsert([1,3,5,6],2)))
    print('Exception :')
    print('1')
    print()
    
    print('Example 3:')
    print('Input : ')
    print('nums = [1,3,5,6], target = 7')
    print('Output :')
    print(str(Solution().searchInsert([1,3,5,6],7)))
    print('Exception :')
    print('4')
    print()
    
    print('Example 4:')
    print('Input : ')
    print('nums = [1,3,5,6], target = 0')
    print('Output :')
    print(str(Solution().searchInsert([1,3,5,6],0)))
    print('Exception :')
    print('0')
    print()
    
    print('Example 5:')
    print('Input : ')
    print('nums = [1], target = 0')
    print('Output :')
    print(str(Solution().searchInsert([1],0)))
    print('Exception :')
    print('0')
    print()
    
    pass
# @lc main=end