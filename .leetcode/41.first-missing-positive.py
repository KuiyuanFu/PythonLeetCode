# @lc app=leetcode id=41 lang=python3
#
# [41] First Missing Positive
#
# https://leetcode.com/problems/first-missing-positive/description/
#
# algorithms
# Hard (33.92%)
# Likes:    5533
# Dislikes: 976
# Total Accepted:    468.5K
# Total Submissions: 1.4M
# Testcase Example:  '[1,2,0]'
#
# Given an unsorted integer array nums, find the smallest missing positive
# integer.
#
#
# Example 1:
# Input: nums = [1,2,0]
# Output: 3
# Example 2:
# Input: nums = [3,4,-1,1]
# Output: 2
# Example 3:
# Input: nums = [7,8,9,11,12]
# Output: 1
#
#
# Constraints:
#
#
# 0 <= nums.length <= 300
# -2^31 <= nums[i] <= 2^31 - 1
#
#
#
# Follow up: Could you implement an algorithm that runs in O(n) time and uses
# constant extra space?
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
# 求无序数组中，缺少的最小的正数。
# 空间 n 的算法很容易，但是要求 空间 1， 时间 n。
# 利用已有空间，存储此位置上的值是否已经存在。因为缺少的正数大小不可能超过长度，所以空间是足够的。
# 设0为标志，第一次循环改所有的0为-1，去掉干扰。
# 第二次循环，读取值，设置对应索引的标志位，使用递归算法，防止覆盖，最多两次循环。
# 第三次循环，检测。
#
# @lc idea=end

# @lc group=

# @lc rank=

# @lc code=start
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        self.nums = nums
        # 去掉干扰
        for i in range(len(self.nums)):
            if nums[i] == 0:
                nums[i] = -1
        # 设置值
        for i, n in enumerate(self.nums):
            self.setFlag(i, n)
        # 检测
        l = 0
        while l < len(self.nums):
            if self.nums[l] != 0:
                break
            l += 1
        return l+1

    def setFlag(self, index, num):
        if 0 < num <= len(self.nums):
            i = num - 1
            n = self.nums[i]
            self.nums[i] = 0
            self.setFlag(i, n)


        pass
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [1,2,0]')
    print('Output :')
    print(str(Solution().firstMissingPositive([1,2,0])))
    print('Exception :')
    print('3')
    print()
    
    print('Example 2:')
    print('Input : ')
    print('nums = [3,4,-1,1]')
    print('Output :')
    print(str(Solution().firstMissingPositive([3,4,-1,1])))
    print('Exception :')
    print('2')
    print()
    
    print('Example 3:')
    print('Input : ')
    print('nums = [7,8,9,11,12]')
    print('Output :')
    print(str(Solution().firstMissingPositive([7,8,9,11,12])))
    print('Exception :')
    print('1')
    print()
    
    pass
# @lc main=end