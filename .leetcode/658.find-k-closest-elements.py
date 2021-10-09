# @lc app=leetcode id=658 lang=python3
#
# [658] Find K Closest Elements
#
# https://leetcode.com/problems/find-k-closest-elements/description/
#
# algorithms
# Medium (43.45%)
# Likes:    3266
# Dislikes: 364
# Total Accepted:    221K
# Total Submissions: 506.8K
# Testcase Example:  '[1,2,3,4,5]\n4\n3'
#
# Given a sorted integer array arr, two integers k and x, return the k closest
# integers to x in the array. The result should also be sorted in ascending
# order.
#
# An integer a is closer to x than an integer b if:
#
#
# |a - x| < |b - x|, or
# |a - x| == |b - x| and a < b
#
#
#
# Example 1:
# Input: arr = [1,2,3,4,5], k = 4, x = 3
# Output: [1,2,3,4]
# Example 2:
# Input: arr = [1,2,3,4,5], k = 4, x = -1
# Output: [1,2,3,4]
#
#
# Constraints:
#
#
# 1 <= k <= arr.length
# 1 <= arr.length <= 10^4
# arr is sorted in ascending order.
# -10^4 <= arr[i], x <= 10^4
#
#
#

# @lc tags=binary-search

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 找最接近给定值的k个数。
# 优先队列。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        h = []
        for n in arr:
            if len(h) < k:
                heappush(h, (-abs(n - x), -n))
            else:
                heappushpop(h, (-abs(n - x), -n))
        res = [-n for _, n in h]
        res.sort()
        return res

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('arr = [1,2,3,4,5], k = 4, x = 3')
    print('Exception :')
    print('[1,2,3,4]')
    print('Output :')
    print(str(Solution().findClosestElements([1, 2, 3, 4, 5], 4, 3)))
    print()

    print('Example 2:')
    print('Input : ')
    print('arr = [1,2,3,4,5], k = 4, x = -1')
    print('Exception :')
    print('[1,2,3,4]')
    print('Output :')
    print(str(Solution().findClosestElements([1, 2, 3, 4, 5], 4, -1)))
    print()

    pass
# @lc main=end