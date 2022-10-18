# @lc app=leetcode id=1013 lang=python3
#
# [1013] Partition Array Into Three Parts With Equal Sum
#
# https://leetcode.com/problems/partition-array-into-three-parts-with-equal-sum/description/
#
# algorithms
# Easy (43.48%)
# Likes:    1323
# Dislikes: 130
# Total Accepted:    71.9K
# Total Submissions: 165.4K
# Testcase Example:  '[0,2,1,-6,6,-7,9,1,2,0,1]'
#
# Given an array of integers arr, return true if we can partition the array
# into three non-empty parts with equal sums.
#
# Formally, we can partition the array if we can find indexes i + 1 < j with
# (arr[0] + arr[1] + ... + arr[i] == arr[i + 1] + arr[i + 2] + ... + arr[j - 1]
# == arr[j] + arr[j + 1] + ... + arr[arr.length - 1])
#
#
# Example 1:
#
#
# Input: arr = [0,2,1,-6,6,-7,9,1,2,0,1]
# Output: true
# Explanation: 0 + 2 + 1 = -6 + 6 - 7 + 9 + 1 = 2 + 0 + 1
#
#
# Example 2:
#
#
# Input: arr = [0,2,1,-6,6,7,9,-1,2,0,1]
# Output: false
#
#
# Example 3:
#
#
# Input: arr = [3,3,6,5,-2,2,5,1,-9,4]
# Output: true
# Explanation: 3 + 3 = 6 = 5 - 2 + 2 + 5 + 1 - 9 + 4
#
#
#
# Constraints:
#
#
# 3 <= arr.length <= 5 * 10^4
# -10^4 <= arr[i] <= 10^4
#
#
#

# @lc tags=array

# @lc imports=start
from operator import length_hint
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定数组，判断是否可以分成相等的三份，即每部分元素和相同
# 滑动窗口
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:

    def canThreePartsEqualSum(self, arr: List[int]) -> bool:

        s = sum(arr)

        if s % 3 != 0:
            return False
        t = s // 3
        s1, s2, s3 = 0, 0, s
        i1, i2 = 0, 0
        length = len(arr)
        while i1 < length:
            n1 = arr[i1]
            s1 += n1
            s2 -= n1
            if s1 == t:
                while i2 < length:
                    n2 = arr[i2]
                    s2 += n2
                    s3 -= n2
                    if i1 < i2 and i2 < length - 1 and s2 == t and s3 == t:
                        return True

                    i2 += 1
            i1 += 1

        return False

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('arr = [0,2,1,-6,6,-7,9,1,2,0,1]')
    print('Exception :')
    print('true')
    print('Output :')
    print(
        str(Solution().canThreePartsEqualSum(
            [0, 2, 1, -6, 6, -7, 9, 1, 2, 0, 1])))
    print()

    print('Example 2:')
    print('Input : ')
    print('arr = [0,2,1,-6,6,7,9,-1,2,0,1]')
    print('Exception :')
    print('false')
    print('Output :')
    print(
        str(Solution().canThreePartsEqualSum(
            [0, 2, 1, -6, 6, 7, 9, -1, 2, 0, 1])))
    print()

    print('Example 3:')
    print('Input : ')
    print('arr = [3,3,6,5,-2,2,5,1,-9,4]')
    print('Exception :')
    print('true')
    print('Output :')
    print(
        str(Solution().canThreePartsEqualSum([3, 3, 6, 5, -2, 2, 5, 1, -9,
                                              4])))
    print()

    pass
# @lc main=end