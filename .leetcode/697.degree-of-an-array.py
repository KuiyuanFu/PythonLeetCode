# @lc app=leetcode id=697 lang=python3
#
# [697] Degree of an Array
#
# https://leetcode.com/problems/degree-of-an-array/description/
#
# algorithms
# Easy (54.99%)
# Likes:    1646
# Dislikes: 1101
# Total Accepted:    127.9K
# Total Submissions: 232K
# Testcase Example:  '[1,2,2,3,1]'
#
# Given a non-empty array of non-negative integers nums, the degree of this
# array is defined as the maximum frequency of any one of its elements.
#
# Your task is to find the smallest possible length of a (contiguous) subarray
# of nums, that has the same degree as nums.
#
#
# Example 1:
#
#
# Input: nums = [1,2,2,3,1]
# Output: 2
# Explanation:
# The input array has a degree of 2 because both elements 1 and 2 appear twice.
# Of the subarrays that have the same degree:
# [1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
# The shortest length is 2. So return 2.
#
#
# Example 2:
#
#
# Input: nums = [1,2,2,3,1,4,2]
# Output: 6
# Explanation:
# The degree is 3 because the element 2 is repeated 3 times.
# So [2,2,3,1,4,2] is the shortest subarray, therefore returning 6.
#
#
#
# Constraints:
#
#
# nums.length will be between 1 and 50,000.
# nums[i] will be an integer between 0 and 49,999.
#
#
#

# @lc tags=array

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 找频数与数组最大值相同的最短字串。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        d = {}
        for i, n in enumerate(nums):
            if n in d:
                t = d[n]
                t[0] += 1
                t[2] = i
            else:
                d[n] = [1, i, i]
        l = 0
        for t in d.values():

            l = max(l, t[0])

        res = len(nums)
        for t in d.values():
            if t[0] == l:
                res = min(res, t[2] - t[1] + 1)
        return res
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [1,2,2,3,1]')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().findShortestSubArray([1, 2, 2, 3, 1])))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums = [1,2,2,3,1,4,2]')
    print('Exception :')
    print('6')
    print('Output :')
    print(str(Solution().findShortestSubArray([1, 2, 2, 3, 1, 4, 2])))
    print()

    pass
# @lc main=end