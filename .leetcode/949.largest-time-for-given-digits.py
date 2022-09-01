# @lc app=leetcode id=949 lang=python3
#
# [949] Largest Time for Given Digits
#
# https://leetcode.com/problems/largest-time-for-given-digits/description/
#
# algorithms
# Medium (35.31%)
# Likes:    581
# Dislikes: 935
# Total Accepted:    74.2K
# Total Submissions: 210.2K
# Testcase Example:  '[1,2,3,4]'
#
# Given an array arr of 4 digits, find the latest 24-hour time that can be made
# using each digit exactly once.
#
# 24-hour times are formatted as "HH:MM", where HH is between 00 and 23, and MM
# is between 00 and 59. The earliest 24-hour time is 00:00, and the latest is
# 23:59.
#
# Return the latest 24-hour time in "HH:MM" format. If no valid time can be
# made, return an empty string.
#
#
# Example 1:
#
#
# Input: arr = [1,2,3,4]
# Output: "23:41"
# Explanation: The valid 24-hour times are "12:34", "12:43", "13:24", "13:42",
# "14:23", "14:32", "21:34", "21:43", "23:14", and "23:41". Of these times,
# "23:41" is the latest.
#
#
# Example 2:
#
#
# Input: arr = [5,5,5,5]
# Output: ""
# Explanation: There are no valid 24-hour times as "55:55" is not valid.
#
#
#
# Constraints:
#
#
# arr.length == 4
# 0 <= arr[i] <= 9
#
#
#

# @lc tags=breadth-first-search;minimax

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定四个数字，求最大的时间。
# 排列
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:

    def largestTimeFromDigits(self, arr: List[int]) -> str:
        res = ''
        for i, j, k, l in permutations(arr, 4):
            h = i * 10 + j
            m = k * 10 + l
            if h < 24 and m < 60:
                a = str(i) + str(j) + ':' + str(k) + str(l)
                res = max(res, a)

        return res

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('arr = [1,2,3,4]')
    print('Exception :')
    print('"23:41"')
    print('Output :')
    print(str(Solution().largestTimeFromDigits([1, 2, 3, 4])))
    print()

    print('Example 2:')
    print('Input : ')
    print('arr = [5,5,5,5]')
    print('Exception :')
    print('""')
    print('Output :')
    print(str(Solution().largestTimeFromDigits([5, 5, 5, 5])))
    print()

    pass
# @lc main=end