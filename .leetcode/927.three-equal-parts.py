# @lc app=leetcode id=927 lang=python3
#
# [927] Three Equal Parts
#
# https://leetcode.com/problems/three-equal-parts/description/
#
# algorithms
# Hard (39.38%)
# Likes:    680
# Dislikes: 106
# Total Accepted:    25.9K
# Total Submissions: 65.6K
# Testcase Example:  '[1,0,1,0,1]'
#
# You are given an array arr which consists of only zeros and ones, divide the
# array into three non-empty parts such that all of these parts represent the
# same binary value.
#
# If it is possible, return any [i, j] with i + 1 < j, such that:
#
#
# arr[0], arr[1], ..., arr[i] is the first part,
# arr[i + 1], arr[i + 2], ..., arr[j - 1] is the second part, and
# arr[j], arr[j + 1], ..., arr[arr.length - 1] is the third part.
# All three parts have equal binary values.
#
#
# If it is not possible, return [-1, -1].
#
# Note that the entire part is used when considering what binary value it
# represents. For example, [1,1,0] represents 6 in decimal, not 3. Also,
# leading zeros are allowed, so [0,1,1] and [1,1] represent the same value.
#
#
# Example 1:
# Input: arr = [1,0,1,0,1]
# Output: [0,3]
# Example 2:
# Input: arr = [1,1,0,1,1]
# Output: [-1,-1]
# Example 3:
# Input: arr = [1,1,0,0,1]
# Output: [0,2]
#
#
# Constraints:
#
#
# 3 <= arr.length <= 3 * 10^4
# arr[i] is 0 or 1
#
#
#

# @lc tags=array;math

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 将一个二进制字符串分成三段，每段值相等。
# 根据1的个数，分成三段。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:

    def threeEqualParts(self, arr: List[int]) -> List[int]:
        err = [-1, -1]
        c1 = arr.count(1)
        if c1 % 3 != 0:
            return err
        if c1 == 0:
            return [0, len(arr) - 1]

        c = 0
        tc = set([1, c1 // 3 + 1, c1 // 3 * 2 + 1])
        il = []
        for i, n in enumerate(arr):
            if n == 1:
                c += 1
                if c in tc:
                    il.append(i)

        length = len(arr) - il[2]
        if arr[il[0]:il[0] +
               length] == arr[il[1]:il[1] +
                              length] and arr[il[0]:il[0] +
                                              length] == arr[il[2]:il[2] +
                                                             length]:
            return [il[0] + length - 1, il[1] + length]
        else:
            return err


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('arr = [1,0,1,0,1]')
    print('Exception :')
    print('[0,3]')
    print('Output :')
    print(str(Solution().threeEqualParts([1, 0, 1, 0, 1])))
    print()

    print('Example 2:')
    print('Input : ')
    print('arr = [1,1,0,1,1]')
    print('Exception :')
    print('[-1,-1]')
    print('Output :')
    print(str(Solution().threeEqualParts([1, 1, 0, 1, 1])))
    print()

    print('Example 3:')
    print('Input : ')
    print('arr = [1,1,0,0,1]')
    print('Exception :')
    print('[0,2]')
    print('Output :')
    print(str(Solution().threeEqualParts([1, 1, 0, 0, 1])))
    print()

    pass
# @lc main=end