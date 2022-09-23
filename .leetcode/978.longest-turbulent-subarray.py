# @lc app=leetcode id=978 lang=python3
#
# [978] Longest Turbulent Subarray
#
# https://leetcode.com/problems/longest-turbulent-subarray/description/
#
# algorithms
# Medium (47.53%)
# Likes:    1440
# Dislikes: 176
# Total Accepted:    76.6K
# Total Submissions: 161.1K
# Testcase Example:  '[9,4,2,10,7,8,8,1,9]'
#
# Given an integer array arr, return the length of a maximum size turbulent
# subarray of arr.
#
# A subarray is turbulent if the comparison sign flips between each adjacent
# pair of elements in the subarray.
#
# More formally, a subarray [arr[i], arr[i + 1], ..., arr[j]] of arr is said to
# be turbulent if and only if:
#
#
# For i <= k < j:
#
#
# arr[k] > arr[k + 1] when k is odd, and
# arr[k] < arr[k + 1] when k is even.
#
#
# Or, for i <= k < j:
#
# arr[k] > arr[k + 1] when k is even, and
# arr[k] < arr[k + 1] when k is odd.
#
#
#
#
#
# Example 1:
#
#
# Input: arr = [9,4,2,10,7,8,8,1,9]
# Output: 5
# Explanation: arr[1] > arr[2] < arr[3] > arr[4] < arr[5]
#
#
# Example 2:
#
#
# Input: arr = [4,8,12,16]
# Output: 2
#
#
# Example 3:
#
#
# Input: arr = [100]
# Output: 1
#
#
#
# Constraints:
#
#
# 1 <= arr.length <= 4 * 10^4
# 0 <= arr[i] <= 10^9
#
#
#

# @lc tags=array

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 求最长子数组的长度，满足大小关系交替。
# 直接对比大小关系。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:

    def maxTurbulenceSize(self, arr: List[int]) -> int:
        res = 1
        now = 1
        isUp = True
        for n1, n2 in pairwise(arr):
            if n1 == n2:
                now = 1
            else:
                isUpNow = n1 < n2
                if isUp != isUpNow:
                    now += 1
                else:
                    now = 2
                isUp = isUpNow
                res = max(res, now)
        return res
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('arr = [9,4,2,10,7,8,8,1,9]')
    print('Exception :')
    print('5')
    print('Output :')
    print(str(Solution().maxTurbulenceSize([9, 4, 2, 10, 7, 8, 8, 1, 9])))
    print()

    print('Example 2:')
    print('Input : ')
    print('arr = [4,8,12,16]')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().maxTurbulenceSize([4, 8, 12, 16])))
    print()

    print('Example 3:')
    print('Input : ')
    print('arr = [100]')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().maxTurbulenceSize([100])))
    print()

    pass
# @lc main=end