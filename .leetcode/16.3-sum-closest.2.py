# @lc app=leetcode id=16 lang=python3
#
# [16] 3Sum Closest
#
# https://leetcode.com/problems/3sum-closest/description/
#
# algorithms
# Medium (46.33%)
# Likes:    3080
# Dislikes: 169
# Total Accepted:    570.4K
# Total Submissions: 1.2M
# Testcase Example:  '[-1,2,1,-4]\n1'
#
# Given an array nums of n integers and an integer target, find three integers
# in nums such that the sum is closest to target. Return the sum of the three
# integers. You may assume that each input would have exactly one solution.
#
#
# Example 1:
#
#
# Input: nums = [-1,2,1,-4], target = 1
# Output: 2
# Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 =
# 2).
#
#
#
# Constraints:
#
#
# 3 <= nums.length <= 10^3
# -10^3 <= nums[i] <= 10^3
# -10^4 <= target <= 10^4
#
#
#


# @lc tags=array;two-pointers

# @lc imports=start
from imports import *
# @lc imports=end

# @lc idea=start
#
# 使用双指针法。首先确定第一个值，之后在剩下的数组中，使用双指针法找最小的差值。之后判断是否重复来剪枝。
#
# @lc idea=end

# @lc group=

# @lc rank=

# @lc code=start
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        # dic = {}
        # for n in nums:
        #     if not dic.__contains__(n):
        #         dic[n] = 1
        #     elif dic[n] < 3:
        #         dic[n] += 1
        # nums = []
        # for i in list(dic.keys()):
        #     nums += [i]*dic[i]
        nums.sort()
        s = nums[0] + nums[1] + nums[2]
        dif = abs(s - target)
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l = i+1
            r = len(nums) - 1
            t = target - nums[i]
            while l < r:
                if abs(t - nums[l] - nums[r]) < dif:
                    dif = abs(t - nums[l] - nums[r])
                    s = nums[i] + nums[l] + nums[r]
                if t - nums[l] - nums[r] > 0:
                    l = l + 1
                else:
                    r = r - 1
            if dif == 0:
                break
        return s


        pass
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [-1,2,1,-4], target = 1')
    print('Output :')
    print(str(Solution().threeSumClosest([-1,2,1,-4],1)))
    print('Exception :')
    print('2')
    print()
    
    pass
# @lc main=end