# @lc app=leetcode id=228 lang=python3
#
# [228] Summary Ranges
#
# https://leetcode.com/problems/summary-ranges/description/
#
# algorithms
# Easy (43.07%)
# Likes:    1080
# Dislikes: 738
# Total Accepted:    219.5K
# Total Submissions: 508K
# Testcase Example:  '[0,1,2,4,5,7]'
#
# You are given a sorted unique integer array nums.
#
# Return the smallest sorted list of ranges that cover all the numbers in the
# array exactly. That is, each element of nums is covered by exactly one of the
# ranges, and there is no integer x such that x is in one of the ranges but not
# in nums.
#
# Each range [a,b] in the list should be output as:
#
#
# "a->b" if a != b
# "a" if a == b
#
#
#
# Example 1:
#
#
# Input: nums = [0,1,2,4,5,7]
# Output: ["0->2","4->5","7"]
# Explanation: The ranges are:
# [0,2] --> "0->2"
# [4,5] --> "4->5"
# [7,7] --> "7"
#
#
# Example 2:
#
#
# Input: nums = [0,2,3,4,6,8,9]
# Output: ["0","2->4","6","8->9"]
# Explanation: The ranges are:
# [0,0] --> "0"
# [2,4] --> "2->4"
# [6,6] --> "6"
# [8,9] --> "8->9"
#
#
# Example 3:
#
#
# Input: nums = []
# Output: []
#
#
# Example 4:
#
#
# Input: nums = [-1]
# Output: ["-1"]
#
#
# Example 5:
#
#
# Input: nums = [0]
# Output: ["0"]
#
#
#
# Constraints:
#
#
# 0 <= nums.length <= 20
# -2^31 <= nums[i] <= 2^31 - 1
# All the values of nums are unique.
# nums is sorted in ascending order.
#
#
#

# @lc tags=array

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 将一个有序数组，合并成区间形式。
# 直接遍历。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ret = []
        if not nums:
            return ret

        l = nums[0]
        i = 1
        while i < len(nums):
            if nums[i] != nums[i - 1] + 1:
                if l == nums[i - 1]:
                    ret.append(str(l))
                else:
                    ret.append(str(l) + '->' + str(nums[i - 1]))
                l = nums[i]
            i += 1
        if l == nums[i - 1]:
            ret.append(str(l))
        else:
            ret.append(str(l) + '->' + str(nums[i - 1]))

        return ret


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [0,1,2,4,5,7]')
    print('Exception :')
    print('["0->2","4->5","7"]')
    print('Output :')
    print(str(Solution().summaryRanges([0, 1, 2, 4, 5, 7])))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums = [0,2,3,4,6,8,9]')
    print('Exception :')
    print('["0","2->4","6","8->9"]')
    print('Output :')
    print(str(Solution().summaryRanges([0, 2, 3, 4, 6, 8, 9])))
    print()

    print('Example 3:')
    print('Input : ')
    print('nums = []')
    print('Exception :')
    print('[]')
    print('Output :')
    print(str(Solution().summaryRanges([])))
    print()

    print('Example 4:')
    print('Input : ')
    print('nums = [-1]')
    print('Exception :')
    print('["-1"]')
    print('Output :')
    print(str(Solution().summaryRanges([-1])))
    print()

    print('Example 5:')
    print('Input : ')
    print('nums = [0]')
    print('Exception :')
    print('["0"]')
    print('Output :')
    print(str(Solution().summaryRanges([0])))
    print()

    pass
# @lc main=end