# @lc app=leetcode id=852 lang=python3
#
# [852] Peak Index in a Mountain Array
#
# https://leetcode.com/problems/peak-index-in-a-mountain-array/description/
#
# algorithms
# Easy (70.96%)
# Likes:    2274
# Dislikes: 1596
# Total Accepted:    336.6K
# Total Submissions: 475K
# Testcase Example:  '[0,1,0]'
#
# Let's call an array arr a mountain if the following properties hold:
#
#
# arr.length >= 3
# There exists some i with 0 < i < arr.length - 1 such that:
#
# arr[0] < arr[1] < ... arr[i-1] < arr[i]
# arr[i] > arr[i+1] > ... > arr[arr.length - 1]
#
#
#
#
# Given an integer array arr that is guaranteed to be a mountain, return any i
# such that arr[0] < arr[1] < ... arr[i - 1] < arr[i] > arr[i + 1] > ... >
# arr[arr.length - 1].
#
#
# Example 1:
#
#
# Input: arr = [0,1,0]
# Output: 1
#
#
# Example 2:
#
#
# Input: arr = [0,2,1,0]
# Output: 1
#
#
# Example 3:
#
#
# Input: arr = [0,10,5,2]
# Output: 1
#
#
#
# Constraints:
#
#
# 3 <= arr.length <= 10^4
# 0 <= arr[i] <= 10^6
# arr is guaranteed to be a mountain array.
#
#
#
# Follow up: Finding the O(n) is straightforward, could you find an O(log(n))
# solution?
#

# @lc tags=array

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 山顶
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:

        l, r = 0, len(arr) - 1

        while r - l > 2:
            m = (l + r) // 2
            if arr[m] < arr[m + 1]:
                l = m
            else:
                r = m + 1

        return l + 1

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('arr = [0,1,0]')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().peakIndexInMountainArray([0, 1, 0])))
    print()

    print('Example 2:')
    print('Input : ')
    print('arr = [0,2,1,0]')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().peakIndexInMountainArray([0, 2, 1, 0])))
    print()

    print('Example 3:')
    print('Input : ')
    print('arr = [0,10,5,2]')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().peakIndexInMountainArray([0, 10, 5, 2])))
    print()

    pass
# @lc main=end