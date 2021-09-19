# @lc app=leetcode id=503 lang=python3
#
# [503] Next Greater Element II
#
# https://leetcode.com/problems/next-greater-element-ii/description/
#
# algorithms
# Medium (60.08%)
# Likes:    3257
# Dislikes: 108
# Total Accepted:    164.6K
# Total Submissions: 273.2K
# Testcase Example:  '[1,2,1]'
#
# Given a circular integer array nums (i.e., the next element of
# nums[nums.length - 1] is nums[0]), return the next greater number for every
# element in nums.
#
# The next greater number of a number x is the first greater number to its
# traversing-order next in the array, which means you could search circularly
# to find its next greater number. If it doesn't exist, return -1 for this
# number.
#
#
# Example 1:
#
#
# Input: nums = [1,2,1]
# Output: [2,-1,2]
# Explanation: The first 1's next greater number is 2;
# The number 2 can't find next greater number.
# The second 1's next greater number needs to search circularly, which is also
# 2.
#
#
# Example 2:
#
#
# Input: nums = [1,2,3,4,3]
# Output: [2,3,4,-1,4]
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 10^4
# -10^9 <= nums[i] <= 10^9
#
#
#

# @lc tags=stack

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 下一个最大的数，循环。
# 两次迭代
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:

        s = []
        buffer = [-1] * len(nums)
        for _ in range(2):
            for i in reversed(range(len(nums))):
                n = nums[i]
                while s and s[-1] <= n:
                    s.pop()
                if s:
                    buffer[i] = s[-1]
                s.append(n)
        return buffer
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [1,2,1]')
    print('Exception :')
    print('[2,-1,2]')
    print('Output :')
    print(str(Solution().nextGreaterElements([1, 2, 1])))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums = [1,2,3,4,3]')
    print('Exception :')
    print('[2,3,4,-1,4]')
    print('Output :')
    print(str(Solution().nextGreaterElements([1, 2, 3, 4, 3])))
    print()

    pass
# @lc main=end