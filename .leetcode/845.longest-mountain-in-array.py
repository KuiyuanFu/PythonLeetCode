# @lc app=leetcode id=845 lang=python3
#
# [845] Longest Mountain in Array
#
# https://leetcode.com/problems/longest-mountain-in-array/description/
#
# algorithms
# Medium (39.69%)
# Likes:    1797
# Dislikes: 55
# Total Accepted:    87.2K
# Total Submissions: 219.5K
# Testcase Example:  '[2,1,4,7,3,2,5]'
#
# You may recall that an array arr is a mountain array if and only if:
#
#
# arr.length >= 3
# There exists some index i (0-indexed) with 0 < i < arr.length - 1 such
# that:
#
# arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
# arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
#
#
#
#
# Given an integer array arr, return the length of the longest subarray, which
# is a mountain. Return 0 if there is no mountain subarray.
#
#
# Example 1:
#
#
# Input: arr = [2,1,4,7,3,2,5]
# Output: 5
# Explanation: The largest mountain is [1,4,7,3,2] which has length 5.
#
#
# Example 2:
#
#
# Input: arr = [2,2,2]
# Output: 0
# Explanation: There is no mountain.
#
#
#
# Constraints:
#
#
# 1 <= arr.length <= 10^4
# 0 <= arr[i] <= 10^4
#
#
#
# Follow up:
#
#
# Can you solve it using only one pass?
# Can you solve it in O(1) space?
#
#
#

# @lc tags=Unknown

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 最长的子字符串，满足一个山。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        res = 0

        l, r = 0, 0
        for i in range(1, len(arr)):
            d = arr[i] - arr[i - 1]
            # flat
            if d == 0:
                l, r = 0, 0
            # up
            elif d > 0:
                # continue up
                if r == 0:
                    l += 1 + (1 if l == 0 else 0)
                # turn
                else:
                    l, r = 2, 0
            #  down
            elif d < 0:
                # continue down after up
                if l > 0:
                    r += 1
                    res = max(res, l + r)
        return res
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('arr = [2,1,4,7,3,2,5]')
    print('Exception :')
    print('5')
    print('Output :')
    print(str(Solution().longestMountain([2, 1, 4, 7, 3, 2, 5])))
    print()

    print('Example 2:')
    print('Input : ')
    print('arr = [2,2,2]')
    print('Exception :')
    print('0')
    print('Output :')
    print(str(Solution().longestMountain([2, 2, 2])))
    print()

    pass
# @lc main=end