# @lc app=leetcode id=941 lang=python3
#
# [941] Valid Mountain Array
#
# https://leetcode.com/problems/valid-mountain-array/description/
#
# algorithms
# Easy (33.58%)
# Likes:    2294
# Dislikes: 149
# Total Accepted:    320.1K
# Total Submissions: 953.4K
# Testcase Example:  '[2,1]'
#
# Given an array of integers arr, return true if and only if it is a valid
# mountain array.
#
# Recall that arr is a mountain array if and only if:
#
#
# arr.length >= 3
# There exists some i with 0 < i < arr.length - 1 such that:
#
# arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
# arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
#
#
#
#
#
# Example 1:
# Input: arr = [2,1]
# Output: false
# Example 2:
# Input: arr = [3,5,5]
# Output: false
# Example 3:
# Input: arr = [0,3,2,1]
# Output: true
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

# @lc tags=array

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 判断数组是否为一个严格的山峰。
# 直接遍历。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:

    def validMountainArray(self, arr: List[int]) -> bool:

        # length >= 3
        if not len(arr) >= 3:
            return False

        # start with up, end with down
        if not (arr[0] < arr[1] and arr[-2] > arr[-1]):
            return False

        # True is up, False is down
        flag = True
        for idx in range(len(arr) - 1):
            # must not equal
            if arr[idx] == arr[idx + 1]:
                return False
            # up or down
            if (arr[idx] < arr[idx + 1]) == flag:
                continue
            else:
                # up turn to down
                if flag:
                    flag = False
                # down can not turn to up
                else:
                    return False
        return True


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('arr = [2,1]')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().validMountainArray([2, 1])))
    print()

    print('Example 2:')
    print('Input : ')
    print('arr = [3,5,5]')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().validMountainArray([3, 5, 5])))
    print()

    print('Example 3:')
    print('Input : ')
    print('arr = [0,3,2,1]')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().validMountainArray([0, 3, 2, 1])))
    print()

    pass
# @lc main=end