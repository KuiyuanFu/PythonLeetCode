# @lc app=leetcode id=930 lang=python3
#
# [930] Binary Subarrays With Sum
#
# https://leetcode.com/problems/binary-subarrays-with-sum/description/
#
# algorithms
# Medium (49.07%)
# Likes:    1368
# Dislikes: 47
# Total Accepted:    47.3K
# Total Submissions: 96.2K
# Testcase Example:  '[1,0,1,0,1]\n2'
#
# Given a binary array nums and an integer goal, return the number of non-empty
# subarrays with a sum goal.
#
# A subarray is a contiguous part of the array.
#
#
# Example 1:
#
#
# Input: nums = [1,0,1,0,1], goal = 2
# Output: 4
# Explanation: The 4 subarrays are bolded and underlined below:
# [1,0,1,0,1]
# [1,0,1,0,1]
# [1,0,1,0,1]
# [1,0,1,0,1]
#
#
# Example 2:
#
#
# Input: nums = [0,0,0,0,0], goal = 0
# Output: 15
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 3 * 10^4
# nums[i] is either 0 or 1.
# 0 <= goal <= nums.length
#
#

# @lc tags=tree;recursion

# @lc imports=start

import math
from imports import *

# @lc imports=end

# @lc idea=start
#
# 二进制子数组和。
# 双指针。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:

    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:

        res = 0
        length = len(nums)
        if goal == 0:
            left, right = 0, 0
            while left < length:
                while left < length and nums[left] == 1:
                    left += 1
                right = left
                while right < length and nums[right] == 0:
                    right += 1

                windowSize = right - left
                res += (windowSize + 1) * windowSize // 2
                left = right
        else:

            ls = [1]
            for n in nums:
                if n == 0:
                    ls[-1] += 1
                else:
                    ls.append(1)
            for left in range(0, len(ls) - goal):
                right = left + goal
                res += ls[left] * ls[right]

        return res

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [1,0,1,0,1], goal = 2')
    print('Exception :')
    print('4')
    print('Output :')
    print(str(Solution().numSubarraysWithSum([1, 0, 1, 0, 1], 2)))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums = [0,0,0,0,0], goal = 0')
    print('Exception :')
    print('15')
    print('Output :')
    print(str(Solution().numSubarraysWithSum([0, 0, 0, 0, 0], 0)))
    print()

    pass
# @lc main=end